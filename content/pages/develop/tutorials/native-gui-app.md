Title: Develop Native GUI Application
save_as: develop/tutorials/native-gui-app.html
url: develop/tutorials/native-gui-app.html

Native system apps in webOS Uses Qt, but Qt version varies between system versions.

For maximum compatibility, this tutorial shows how to build GUI application with SDL2.

This project is written in C11, and it can run through webOS 1 to webOS 6 without any issue.

## Config CMake Project

Start with project declaration.

```cmake
cmake_minimum_required (VERSION 3.8)

# This is a C/C++ project
project ("myapp" VERSION 1.0 LANGUAGES C CXX)

# Use `pkg-config` to link needed libraries.
find_package(PkgConfig REQUIRED)

# Use SDL2 for window creation and event handling.
pkg_check_modules(SDL2 REQUIRED sdl2)

# Add source to this project's executable.
add_executable (myapp "src/myapp.c")

# Link SDL2
target_include_directories("myapp" SYSTEM PRIVATE ${SDL2_INCLUDE_DIRS})
target_link_libraries("myapp" PRIVATE ${SDL2_LIBRARIES})
```

## Create an empty app with SDL2 and LVGL

Add `lv_conf.h`. `#defines` below are important to have, for other settings you can set based on your use case.

```c
/* Use 32-bit color depth */
#define LV_COLOR_DEPTH     32

/* Use stdlib to allocate/free memory */
#define LV_MEM_CUSTOM      1
#define LV_MEM_CUSTOM_INCLUDE   <string.h>   /*Header for the dynamic memory function*/
#define LV_MEM_CUSTOM_ALLOC     malloc
#define LV_MEM_CUSTOM_FREE      free
#define LV_MEM_CUSTOM_REALLOC   realloc

/* Use the standard `memcpy` and `memset` instead of LVGL's own functions. */
#define LV_MEMCPY_MEMSET_STD    1

/* Let LVGL call SDL_GetTicks automatically so we can skip creating a separate timer thread. */
#define LV_TICK_CUSTOM     1
#define LV_TICK_CUSTOM_INCLUDE  <SDL.h>
#define LV_TICK_CUSTOM_SYS_TIME_EXPR (SDL_GetTicks())

#define LV_DRAW_COMPLEX 1
#define LV_SHADOW_CACHE_SIZE    0
#define LV_IMG_CACHE_DEF_SIZE       0

/* Use SDL draw backend */
#define LV_USE_GPU_SDL    1
#define LV_GPU_SDL_INCLUDE_PATH <SDL.h>
```

Edit `src/myapp.c`.

```c
static void process_events();

static lv_disp_t *display_init(SDL_Window *window);

static void flush_cb(lv_disp_drv_t *disp_drv, const lv_area_t *area, lv_color_t *src);

static bool running = true;

int main(int argc, char *argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    lv_init();

    int w = 800, h = 480;
    SDL_DisplayMode mode;
    SDL_GetDisplayMode(0, 0, &mode);
    /* Get display size. Fallback to 1920x1080 if failed. */
    if (mode.w > 0 && mode.h > 0) {
        w = mode.w;
        h = mode.h;
    }
    /* Caveat: Don't use SDL_WINDOW_FULLSCREEN_DESKTOP on webOS. On older platforms it's not supported. */
    SDL_Window *window = SDL_CreateWindow("myapp", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, w, h,
                                          SDL_WINDOW_FULLSCREEN | SDL_WINDOW_ALLOW_HIGHDPI);
    lv_disp_t *disp = display_init(window);
    lv_disp_set_default(disp);

    lv_obj_t *label = lv_label_create(lv_scr_act());
    lv_obj_set_pos(label, LV_DPX(10), LV_DPX(10));
    lv_label_set_text(label, "Hello, world!");

    while (running) {
        process_events();
        lv_task_handler();
        SDL_Delay(1);
    }
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
```

Implement functions declared above

```c

static void process_events() {
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        switch (event.type) {
            case SDL_QUIT:
                running = false;
                break;
            default:
                break;
        }
    }
}

static lv_disp_t *display_init(SDL_Window *window) {
    int width, height;
    SDL_GetWindowSize(window, &width, &height);
    SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "1");
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    lv_disp_draw_buf_t *draw_buf = malloc(sizeof(lv_disp_draw_buf_t));
    SDL_Texture *texture = lv_draw_sdl_create_screen_texture(renderer, width, height);
    lv_disp_draw_buf_init(draw_buf, texture, NULL, width * height);
    lv_disp_drv_t *driver = malloc(sizeof(lv_disp_drv_t));
    lv_disp_drv_init(driver);

    lv_draw_sdl_drv_param_t *param = lv_mem_alloc(sizeof(lv_draw_sdl_drv_param_t));
    param->renderer = renderer;
    driver->user_data = param;
    driver->draw_buf = draw_buf;
    driver->flush_cb = flush_cb;
    driver->hor_res = width;
    driver->ver_res = height;
    SDL_SetRenderTarget(renderer, texture);
    lv_disp_t *disp = lv_disp_drv_register(driver);
    return disp;
}

static void flush_cb(lv_disp_drv_t *disp_drv, const lv_area_t *area, lv_color_t *src) {
    LV_UNUSED(src);
    if (area->x2 < 0 || area->y2 < 0 ||
        area->x1 > disp_drv->hor_res - 1 || area->y1 > disp_drv->ver_res - 1) {
        lv_disp_flush_ready(disp_drv);
        return;
    }

    if (lv_disp_flush_is_last(disp_drv)) {
        lv_draw_sdl_drv_param_t *param = disp_drv->user_data;
        SDL_Renderer *renderer = param->renderer;
        SDL_Texture *texture = disp_drv->draw_buf->buf1;
        SDL_SetRenderTarget(renderer, NULL);
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
        SDL_RenderClear(renderer);
        SDL_SetTextureBlendMode(texture, SDL_BLENDMODE_BLEND);
        SDL_RenderCopy(renderer, texture, NULL, NULL);
        SDL_RenderPresent(renderer);
        SDL_SetRenderTarget(renderer, texture);
    }
    lv_disp_flush_ready(disp_drv);
}
```

Now if you build the project, you should be able to get a binary. If you build the project with system toolchain, you'll
be able to run it, and see "Hello, world!" on top left corner.

Next, we configure CMake to generate IPK for installing on TV.

## Create Installation Package

### Create `appinfo.json`

```json
{
  "id": "com.mycompany.myapp",
  "type": "native",
  "main": "myapp",
  "icon": "icon.png",
  "title": "Native App",
  "version": "0.0.1"
}
```

### Config CPack

Append to `CMakeLists.txt`.

```cmake
install(TARGETS myapp RUNTIME DESTINATION .)
install(FILES appinfo.json icon.png DESTINATION .)

set(CPACK_GENERATOR "External")
set(CPACK_EXTERNAL_PACKAGE_SCRIPT "${CMAKE_SOURCE_DIR}/AresPackage.cmake")
set(CPACK_EXTERNAL_ENABLE_STAGING TRUE)
set(CPACK_MONOLITHIC_INSTALL TRUE)

include(CPack)
```

Create `AresPackage.cmake`

```cmake
execute_process(COMMAND ares-package "${CPACK_TEMPORARY_DIRECTORY}")
```

### Input Handling

#### Magic Remote (Mouse)

#### Remote Keys (Keyboard)

#### Bonus: Gamepad

### Shipping with Dependencies

## Tips

### Remote GDB Debugging

### Cross-Platform Program for Easier Debugging

## Compatibility

### SDL Version Support Chart
