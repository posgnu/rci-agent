#!/bin/bash

environments=(
    "choose-list"
    "click-button-sequence"
    "click-button"
    "click-checkboxes-large"
    "click-checkboxes-soft"
    "click-checkboxes-transfer"
    "click-checkboxes"
    "click-collapsible-2"
    "click-collapsible"
    "click-color"
    "click-dialog-2"
    "click-dialog"
    "click-link"
    "click-menu"
    "click-option"
    "click-scroll-list"
    "click-shades"
    "click-tab-2-hard"
    "click-tab-2"
    "click-tab"
    "click-test-2"
    "click-test"
    "click-widget"
)

llm="chatgpt-16"
num_episodes=1
irci=1
erci=0

for env in "${environments[@]}"
do
    if [[ "$env" == "choose-list" ]]; then
        llm="chatgpt"
        erci=1
    else
        llm="chatgpt-16"
        erci=0
    fi

    command="python main.py --env $env --llm $llm --num-episodes $num_episodes --irci $irci --erci $erci"
    echo "Executing: $command"
    eval $command
done
