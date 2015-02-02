#! /bin/zsh
# A script to make using 256 colors in zsh less painful.
# P.C. Shyamshankar <sykora@lucentbeing.com>
# Copied from http://github.com/sykora/etc/blob/master/zsh/functions/spectrum/

typeset -Ag FX FG BG

FX=(
    reset     "%{0m%}"
    bold      "%{1m%}" no-bold      "%{m%}"
    italic    "%{3m%}" no-italic    "%{%}"
    underline "%{4m%}" no-underline "%{%}"
    blink     "%{5m%}" no-blink     "%{m%}"
    reverse   "%{7m%}" no-reverse   "%{%}"
)

for color in {000..255}; do
    FG[$color]="%{;${color}m%}"
    BG[$color]="%{${color}m%}"
done


ZSH_SPECTRUM_TEXT=${ZSH_SPECTRUM_TEXT:-Arma virumque cano Troiae qui primus ab oris}

# Show all 256 colors with color number
function spectrum_ls() {
    for code in {000..255}; do
	print -P -- "$code: %F{$code}$ZSH_SPECTRUM_TEXT%f"
    done
}

# Show all 256 colors where the background is set to specific color
function spectrum_bls() {
    for code in {000..255}; do
	print -P -- "$BG[$code]$code: $ZSH_SPECTRUM_TEXT %{$reset_color%}"
    done
    }
