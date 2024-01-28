package main

import (
	"log"
	"os"

	telegramBotApi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

var token = os.Getenv("TELEGRAM_BOT_API")

func Telegram() {
	bot, err := telegramBotApi.NewBotAPI(token)
	if err != nil {
		log.Fatalln(err)
	}

	bot.Debug = true
}
