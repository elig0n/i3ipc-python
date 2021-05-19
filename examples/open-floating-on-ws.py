#!/usr/bin/env python3

import sys
import i3ipc

if len(sys.argv) < 2:
    print("{}: please specify workspace(s) start string(s)".
          format(sys.argv[0]))
    sys.exit(-1)

# This example shows how to make any window that opens on a workspace floating

# All workspaces that start with a string in this list will have their windows
# open floating
FLOATING_WORKSPACES = []
for arg in sys.argv[1:]:
    FLOATING_WORKSPACES.append(arg)


def is_ws_floating(name):
    for floating_ws in FLOATING_WORKSPACES:
        if name.startswith(floating_ws):
            return True

    return False


i3 = i3ipc.Connection()


def on_window_open(i3, e):
    ws = i3.get_tree().find_focused().workspace()
    if is_ws_floating(ws.name):
        e.container.command('floating toggle')


i3.on('window::new', on_window_open)

i3.main()
