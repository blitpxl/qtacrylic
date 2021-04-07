from ctypes import POINTER, c_bool, sizeof, windll, pointer, c_int
from ctypes.wintypes import DWORD

from win32 import win32api, win32gui
from win32.lib import win32con

from c_structures import ACCENT_POLICY, ACCENT_STATE, WINDOWCOMPOSITIONATTRIB, WINDOWCOMPOSITIONATTRIBDATA


class WindowEffect:
    def __init__(self):
        self.SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
        self.SetWindowCompositionAttribute.restype = c_bool
        self.SetWindowCompositionAttribute.argtypes = [
            c_int, POINTER(WINDOWCOMPOSITIONATTRIBDATA)]

        self.accentPolicy = ACCENT_POLICY()
        self.winCompAttrData = WINDOWCOMPOSITIONATTRIBDATA()
        self.winCompAttrData.Attribute = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY.value[0]
        self.winCompAttrData.SizeOfData = sizeof(self.accentPolicy)
        self.winCompAttrData.Data = pointer(self.accentPolicy)

    def setAcrylicEffect(self, hWnd: int, gradientColor: str = 'F0000000', isEnableShadow: bool = True,
                         animationId: int = 0):

        gradientColor = gradientColor[6:] + gradientColor[4:6] + \
                        gradientColor[2:4] + gradientColor[:2]
        gradientColor = DWORD(int(gradientColor, base=16))
        animationId = DWORD(animationId)
        accentFlags = DWORD(0x20 | 0x40 | 0x80 | 0x100) if isEnableShadow else DWORD(0)

        self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_ACRYLICBLURBEHIND.value[0]
        self.accentPolicy.GradientColor = gradientColor
        self.accentPolicy.AccentFlags = accentFlags
        self.accentPolicy.AnimationId = animationId
        self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

    def setAeroEffect(self, hWnd: int):
        self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND.value[0]
        self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

    @staticmethod
    def moveWindow(hWnd: int):
        win32gui.ReleaseCapture()
        win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND,
                             win32con.SC_MOVE + win32con.HTCAPTION, 0)
