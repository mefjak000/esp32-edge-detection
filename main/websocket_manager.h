#ifndef ESP32_CAM_SCANNER_WEBSOCKET_MANAGER_H
#define ESP32_CAM_SCANNER_WEBSOCKET_MANAGER_H

#include <esp_http_client.h>
#include "esp_camera.h"

// prepare C functions to be called from C++ code
#ifdef __cplusplus
extern "C" {
#endif
    void websocket_init(void);
    void websocket_send(void *pvParameters);
#ifdef __cplusplus
}
#endif
#endif //ESP32_CAM_SCANNER_WEBSOCKET_MANAGER_H
