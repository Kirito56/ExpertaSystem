# ExpertaSystem

- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kirito56/ExpertaSystem/HEAD)
- [![launch @ gesis.org](https://notebooks.gesis.org/binder/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/Kirito56/ExpertaSystem/HEAD)

### 2 engines:
`>> Вкажіть кількість фактів = i` `create folder ES with Facts and Rules`
* Asserts:
	* `i Facts` 
	* `15 Rules` 
	* `Chain connection`
* DefFact 
	* `i Facts` 
	* `15 Rules` 
	* `Chain connection`
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
	* `Clips` template
```c#
(deftemplate Kebab
	(slot Type) // Тип м'яса (Курятина, Свинятина,Кенгуру)
	(slot Action) // Дія (Чекати, Перевертати, Забрати)
	(slot DegreeOfRoastiness)// Ступінь піджаристості (Сире, Піджарилось, Готове, Згоріло)
	(slot AlreadyTurnedOver) // Вже (перевертали/не перевертали)
	(slot PartyReady) // Сторона (готова/не готова)
	(slot DoneOnOneSide) //(Готово/не готово) з однієї сторони
	(slot DoneOnBothSides) // (Готово/Не готово) з обох сторін
	(slot BothSideReady) // (Готова/Не готова) з другої сторони
	(slot DoneAToTheMajority) // (Готова/Не готова) по думці більшості
	(slot Time) // Час запікання шашлика (0-20)
	(multislot NumberOfPeople) // Список людей на яких готовиться шашлик
)
```
