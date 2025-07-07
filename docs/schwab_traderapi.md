Trader API - Account Access and User Preferences
 1.0.0 
OAS3
Schwab Trader API access to Account, Order entry and User Preferences

Contact Schwab Trader API team
Servers

https://api.schwabapi.com/trader/v1
Accounts


GET
/accounts/accountNumbers
Get list of account numbers and their encrypted values


GET
/accounts
Get linked account(s) balances and positions for the logged in user.


GET
/accounts/{accountNumber}
Get a specific account balance and positions for the logged in user.

Orders


GET
/accounts/{accountNumber}/orders
Get all orders for a specific account.


POST
/accounts/{accountNumber}/orders
Place order for a specific account.


GET
/accounts/{accountNumber}/orders/{orderId}
Get a specific order by its ID, for a specific account


DELETE
/accounts/{accountNumber}/orders/{orderId}
Cancel an order for a specific account


PUT
/accounts/{accountNumber}/orders/{orderId}
Replace order for a specific account


GET
/orders
Get all orders for all accounts


POST
/accounts/{accountNumber}/previewOrder
Preview order for a specific account. **Coming Soon**.

Transactions


GET
/accounts/{accountNumber}/transactions
Get all transactions information for a specific account.


GET
/accounts/{accountNumber}/transactions/{transactionId}
Get specific transaction information for a specific account

UserPreference


GET
/userPreference
Get user preference information for the logged in user.


Schemas
AccountNumberHash{
accountNumber	[...]
hashValue	[...]
}
sessionstring
Enum:
Array [ 4 ]
durationstring
Enum:
Array [ 8 ]
orderTypestring
Enum:
Array [ 15 ]
orderTypeRequeststring
Same as orderType, but does not have UNKNOWN since this type is not allowed as an input

Enum:
Array [ 14 ]
complexOrderStrategyTypestring
Enum:
Array [ 21 ]
requestedDestinationstring
Enum:
Array [ 12 ]
stopPriceLinkBasisstring
Enum:
Array [ 9 ]
stopPriceLinkTypestring
Enum:
Array [ 3 ]
stopPriceOffsetnumber($double)
stopTypestring
Enum:
Array [ 5 ]
priceLinkBasisstring
Enum:
Array [ 9 ]
priceLinkTypestring
Enum:
Array [ 3 ]
taxLotMethodstring
Enum:
Array [ 7 ]
specialInstructionstring
Enum:
Array [ 3 ]
orderStrategyTypestring
Enum:
Array [ 9 ]
statusstring
Enum:
Array [ 21 ]
amountIndicatorstring
Enum:
Array [ 5 ]
settlementInstructionstring
Enum:
Array [ 4 ]
OrderStrategy{
accountNumber	[...]
advancedOrderType	[...]
closeTime	[...]
enteredTime	[...]
orderBalance	OrderBalance{...}
orderStrategyType	orderStrategyType[...]
orderVersion	[...]
session	session[...]
status	apiOrderStatus[...]
allOrNone	[...]
discretionary	[...]
duration	duration[...]
filledQuantity	[...]
orderType	orderType[...]
orderValue	[...]
price	[...]
quantity	[...]
remainingQuantity	[...]
sellNonMarginableFirst	[...]
settlementInstruction	settlementInstruction[...]
strategy	complexOrderStrategyType[...]
amountIndicator	amountIndicator[...]
orderLegs	[...]
}
OrderLeg{
askPrice	[...]
bidPrice	[...]
lastPrice	[...]
markPrice	[...]
projectedCommission	[...]
quantity	[...]
finalSymbol	[...]
legId	[...]
assetType	assetType[...]
instruction	instruction[...]
}
OrderBalance{
orderValue	[...]
projectedAvailableFund	[...]
projectedBuyingPower	[...]
projectedCommission	[...]
}
OrderValidationResult{
alerts	[...]
accepts	[...]
rejects	[...]
reviews	[...]
warns	[...]
}
OrderValidationDetail{
validationRuleName	[...]
message	[...]
activityMessage	[...]
originalSeverity	APIRuleAction[...]
overrideName	[...]
overrideSeverity	APIRuleAction[...]
}
APIRuleActionstring
Enum:
Array [ 5 ]
CommissionAndFee{
commission	Commission{...}
fee	Fees{...}
trueCommission	Commission{...}
}
Commission{
commissionLegs	[...]
}
CommissionLeg{
commissionValues	[...]
}
CommissionValue{
value	[...]
type	FeeType[...]
}
Fees{
feeLegs	[...]
}
FeeLeg{
feeValues	[...]
}
FeeValue{
value	[...]
type	FeeType[...]
}
FeeTypestring
Enum:
Array [ 25 ]
Account{
securitiesAccount	SecuritiesAccount{...}
}
DateParam{
date	[...]
}
Order{
session	session[...]
duration	duration[...]
orderType	orderType[...]
cancelTime	[...]
complexOrderStrategyType	complexOrderStrategyType[...]
quantity	[...]
filledQuantity	[...]
remainingQuantity	[...]
requestedDestination	requestedDestination[...]
destinationLinkName	[...]
releaseTime	[...]
stopPrice	[...]
stopPriceLinkBasis	stopPriceLinkBasis[...]
stopPriceLinkType	stopPriceLinkType[...]
stopPriceOffset	[...]
stopType	stopType[...]
priceLinkBasis	priceLinkBasis[...]
priceLinkType	priceLinkType[...]
price	[...]
taxLotMethod	taxLotMethod[...]
orderLegCollection	[...]
activationPrice	[...]
specialInstruction	specialInstruction[...]
orderStrategyType	orderStrategyType[...]
orderId	[...]
cancelable	[...]
editable	[...]
status	status[...]
enteredTime	[...]
closeTime	[...]
tag	[...]
accountNumber	[...]
orderActivityCollection	[...]
replacingOrderCollection	[...]
childOrderStrategies	[...]
statusDescription	[...]
}
OrderRequest{
session	session[...]
duration	duration[...]
orderType	orderTypeRequest[...]
cancelTime	[...]
complexOrderStrategyType	complexOrderStrategyType[...]
quantity	[...]
filledQuantity	[...]
remainingQuantity	[...]
destinationLinkName	[...]
releaseTime	[...]
stopPrice	[...]
stopPriceLinkBasis	stopPriceLinkBasis[...]
stopPriceLinkType	stopPriceLinkType[...]
stopPriceOffset	[...]
stopType	stopType[...]
priceLinkBasis	priceLinkBasis[...]
priceLinkType	priceLinkType[...]
price	[...]
taxLotMethod	taxLotMethod[...]
orderLegCollection	[...]
activationPrice	[...]
specialInstruction	specialInstruction[...]
orderStrategyType	orderStrategyType[...]
orderId	[...]
cancelable	[...]
editable	[...]
status	status[...]
enteredTime	[...]
closeTime	[...]
accountNumber	[...]
orderActivityCollection	[...]
replacingOrderCollection	[...]
childOrderStrategies	[...]
statusDescription	[...]
}
PreviewOrder{
orderId	[...]
orderStrategy	OrderStrategy{...}
orderValidationResult	OrderValidationResult{...}
commissionAndFee	CommissionAndFee{...}
}
OrderActivity{
activityType	[...]
executionType	[...]
quantity	[...]
orderRemainingQuantity	[...]
executionLegs	[...]
}
ExecutionLeg{
legId	[...]
price	[...]
quantity	[...]
mismarkedQuantity	[...]
instrumentId	[...]
time	[...]
}
Position{
shortQuantity	[...]
averagePrice	[...]
currentDayProfitLoss	[...]
currentDayProfitLossPercentage	[...]
longQuantity	[...]
settledLongQuantity	[...]
settledShortQuantity	[...]
agedQuantity	[...]
instrument	AccountsInstrument{...}
marketValue	[...]
maintenanceRequirement	[...]
averageLongPrice	[...]
averageShortPrice	[...]
taxLotAverageLongPrice	[...]
taxLotAverageShortPrice	[...]
longOpenProfitLoss	[...]
shortOpenProfitLoss	[...]
previousSessionLongQuantity	[...]
previousSessionShortQuantity	[...]
currentDayCost	[...]
}
ServiceError{
message	[...]
errors	[...]
}
OrderLegCollection{
orderLegType	[...]
legId	[...]
instrument	AccountsInstrument{...}
instruction	instruction[...]
positionEffect	[...]
quantity	[...]
quantityType	[...]
divCapGains	[...]
toSymbol	[...]
}
SecuritiesAccount{
oneOf ->	
MarginAccount{...}
CashAccount{...}
}
SecuritiesAccountBase{
type	[...]
accountNumber	[...]
roundTrips	[...]
isDayTrader	[...]
isClosingOnlyRestricted	[...]
pfcbFlag	[...]
positions	[...]
}
MarginAccount{
type	[...]
accountNumber	[...]
roundTrips	[...]
isDayTrader	[...]
isClosingOnlyRestricted	[...]
pfcbFlag	[...]
positions	[...]
initialBalances	MarginInitialBalance{...}
currentBalances	MarginBalance{...}
projectedBalances	MarginBalance{...}
}
MarginInitialBalance{
accruedInterest	[...]
availableFundsNonMarginableTrade	[...]
bondValue	[...]
buyingPower	[...]
cashBalance	[...]
cashAvailableForTrading	[...]
cashReceipts	[...]
dayTradingBuyingPower	[...]
dayTradingBuyingPowerCall	[...]
dayTradingEquityCall	[...]
equity	[...]
equityPercentage	[...]
liquidationValue	[...]
longMarginValue	[...]
longOptionMarketValue	[...]
longStockValue	[...]
maintenanceCall	[...]
maintenanceRequirement	[...]
margin	[...]
marginEquity	[...]
moneyMarketFund	[...]
mutualFundValue	[...]
regTCall	[...]
shortMarginValue	[...]
shortOptionMarketValue	[...]
shortStockValue	[...]
totalCash	[...]
isInCall	[...]
unsettledCash	[...]
pendingDeposits	[...]
marginBalance	[...]
shortBalance	[...]
accountValue	[...]
}
MarginBalance{
availableFunds	[...]
availableFundsNonMarginableTrade	[...]
buyingPower	[...]
buyingPowerNonMarginableTrade	[...]
dayTradingBuyingPower	[...]
dayTradingBuyingPowerCall	[...]
equity	[...]
equityPercentage	[...]
longMarginValue	[...]
maintenanceCall	[...]
maintenanceRequirement	[...]
marginBalance	[...]
regTCall	[...]
shortBalance	[...]
shortMarginValue	[...]
sma	[...]
isInCall	[...]
stockBuyingPower	[...]
optionBuyingPower	[...]
}
CashAccount{
type	[...]
accountNumber	[...]
roundTrips	[...]
isDayTrader	[...]
isClosingOnlyRestricted	[...]
pfcbFlag	[...]
positions	[...]
initialBalances	CashInitialBalance{...}
currentBalances	CashBalance{...}
projectedBalances	CashBalance{...}
}
CashInitialBalance{
accruedInterest	[...]
cashAvailableForTrading	[...]
cashAvailableForWithdrawal	[...]
cashBalance	[...]
bondValue	[...]
cashReceipts	[...]
liquidationValue	[...]
longOptionMarketValue	[...]
longStockValue	[...]
moneyMarketFund	[...]
mutualFundValue	[...]
shortOptionMarketValue	[...]
shortStockValue	[...]
isInCall	[...]
unsettledCash	[...]
cashDebitCallValue	[...]
pendingDeposits	[...]
accountValue	[...]
}
CashBalance{
cashAvailableForTrading	[...]
cashAvailableForWithdrawal	[...]
cashCall	[...]
longNonMarginableMarketValue	[...]
totalCash	[...]
cashDebitCallValue	[...]
unsettledCash	[...]
}
TransactionBaseInstrument{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
}
AccountsBaseInstrument{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
}
AccountsInstrument{
oneOf ->	
AccountCashEquivalent{...}
AccountEquity{...}
AccountFixedIncome{...}
AccountMutualFund{...}
AccountOption{...}
}
TransactionInstrument{
oneOf ->	
TransactionCashEquivalent{...}
CollectiveInvestment{...}
Currency{...}
TransactionEquity{...}
TransactionFixedIncome{...}
Forex{...}
Future{...}
Index{...}
TransactionMutualFund{...}
TransactionOption{...}
Product{...}
}
TransactionCashEquivalent{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
}
CollectiveInvestment{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
}
instructionstring
Enum:
Array [ 10 ]
assetTypestring
Enum:
Array [ 11 ]
Currency{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
}
TransactionEquity{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
}
TransactionFixedIncome{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
maturityDate	[...]
factor	[...]
multiplier	[...]
variableRate	[...]
}
Forex{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
baseCurrency	Currency{...}
counterCurrency	Currency{...}
}
Future{
activeContract	[...]
type	[...]
expirationDate	[...]
lastTradingDate	[...]
firstNoticeDate	[...]
multiplier	[...]
oneOf ->	
TransactionCashEquivalent{...}
CollectiveInvestment{...}
Currency{...}
TransactionEquity{...}
TransactionFixedIncome{...}
Forex{...}
{...}
Index{...}
TransactionMutualFund{...}
TransactionOption{...}
Product{...}
}
Index{
activeContract	[...]
type	[...]
oneOf ->	
TransactionCashEquivalent{...}
CollectiveInvestment{...}
Currency{...}
TransactionEquity{...}
TransactionFixedIncome{...}
Forex{...}
Future{...}
{...}
TransactionMutualFund{...}
TransactionOption{...}
Product{...}
}
TransactionMutualFund{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
fundFamilyName	[...]
fundFamilySymbol	[...]
fundGroup	[...]
type	[...]
exchangeCutoffTime	[...]
purchaseCutoffTime	[...]
redemptionCutoffTime	[...]
}
TransactionOption{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
expirationDate	[...]
optionDeliverables	[...]
optionPremiumMultiplier	[...]
putCall	[...]
strikePrice	[...]
type	[...]
underlyingSymbol	[...]
underlyingCusip	[...]
deliverable	TransactionInstrument{...}
}
Product{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
}
AccountCashEquivalent{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
type	[...]
}
AccountEquity{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
}
AccountFixedIncome{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
maturityDate	[...]
factor	[...]
variableRate	[...]
}
AccountMutualFund{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
}
AccountOption{
assetType*	[...]
cusip	[...]
symbol	[...]
description	[...]
instrumentId	[...]
netChange	[...]
optionDeliverables	[...]
putCall	[...]
optionMultiplier	[...]
type	[...]
underlyingSymbol	[...]
}
AccountAPIOptionDeliverable{
symbol	[...]
deliverableUnits	[...]
apiCurrencyType	[...]
assetType	assetType[...]
}
TransactionAPIOptionDeliverable{
rootSymbol	[...]
strikePercent	[...]
deliverableNumber	[...]
deliverableUnits	[...]
deliverable	TransactionInstrument{...}
assetType	assetType[...]
}
apiOrderStatusstring
Enum:
Array [ 21 ]
TransactionTypestring
Enum:
Array [ 15 ]
Transaction{
activityId	[...]
time	[...]
user	UserDetails{...}
description	[...]
accountNumber	[...]
type	TransactionType[...]
status	[...]
subAccount	[...]
tradeDate	[...]
settlementDate	[...]
positionId	[...]
orderId	[...]
netAmount	[...]
activityType	[...]
transferItems	[...]
}
UserDetails{
cdDomainId	[...]
login	[...]
type	[...]
userId	[...]
systemUserName	[...]
firstName	[...]
lastName	[...]
brokerRepCode	[...]
}
TransferItem{
instrument	TransactionInstrument{...}
amount	[...]
cost	[...]
price	[...]
feeType	[...]
positionEffect	[...]
}
UserPreference{
accounts	[...]
streamerInfo	[...]
offers	[...]
}
UserPreferenceAccount{
accountNumber	[...]
primaryAccount	[...]
type	[...]
nickName	[...]
accountColor	[...]
displayAcctId	[...]
autoPositionEffect	[...]
}
StreamerInfo{
streamerSocketUrl	[...]
schwabClientCustomerId	[...]
schwabClientCorrelId	[...]
schwabClientChannel	[...]
schwabClientFunctionId	[...]
}
Offer{
level2Permissions	[...]
mktDataPermission	[...]
}
