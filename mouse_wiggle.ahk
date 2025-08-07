toggle := false

\:: ; Press the "\" key to toggle on/off
    toggle := !toggle
    if (toggle) {
        SetTimer, Wiggle, 100  ; Wiggle every .1 second
    } else {
        SetTimer, Wiggle, Off
    }
return

Wiggle:
    MouseGetPos, x, y     ; Get current mouse position
    Random, dx, 1, 3      ; Random left/right movement (1–3 pixels)

    MouseMove, x + dx, y, 0  ; Move right
    MouseMove, x - dx, y, 0  ; Move left
    MouseMove, x, y, 0       ; Return to original
return
