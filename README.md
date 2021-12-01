# ExpertaSystem

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kirito56/ExpertaSystem/HEAD)

### 2 engines:
`>> Вкажіть кількість фактів = i` `create folder ES with Facts`
* Asserts `i Facts` `15 Rules` `Chain connection`
* DefFact `i Facts` `15 Rules` `Chain connection`
* JSON example 
```json 
{
	"Fact-id": 0,
	"Type": "Курка",
	"Action": "Чекати",
	"DegreeOfRoastiness": "Сире",
	"AlreadyTurnedOver": false,
	"PartyReady": false,
	"DoneOnOneSide": false,
	"DoneOnBothSides": true,
	"BothSideReady": false,
	"DoneAToTheMajority": false,
	"Time": 7,
	"NumberOfPeople": ["Володя", "Женя", "Влад"],
	"Added": "12/1/2021 9:31:12"
},
{
	"Правило 7": {
		"Шукає факт де Тип не свинина або де тип не Кенгуру": "Дія: Перевернути"
		},
	"Added": "12/1/2021 9:31:12"
}
```




### 1 Experta System:
* `Kebab`