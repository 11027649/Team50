import colorama.ansi

# patch in extra ansi styles
colorama.ansi.AnsiStyle.UNDERLINED = 4
colorama.ansi.AnsiStyle.BLINK = 5
colorama.ansi.AnsiStyle.REVERSEVID = 7
colorama.ansi.Style = colorama.ansi.AnsiCodes() #colorama.ansi.AnsiStyle
colorama.Style = colorama.ansi.Style

import colorama
  
if __name__ == "__main__":
    colorama.init()
    print("\x1b[1;1H\x1b[2J-----------------colorama test----------------")
    print(colorama.Style.BRIGHT + "bright" + colorama.Style.RESET_ALL)
    # print(colorama.Style.UNDERLINED + "underlined" + colorama.Style.RESET_ALL)
    # print(colorama.Style.BLINK + "blink" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + colorama.Back.RED + "yellow on red" + colorama.Style.RESET_ALL)
    # print(colorama.Style.REVERSEVID + "reversevid" + colorama.Style.RESET_ALL)
    # print(colorama.Fore.YELLOW + colorama.Back.RED + colorama.Style.REVERSEVID + "yellow on red, reversed" + colorama.Style.RESET_ALL)
  
