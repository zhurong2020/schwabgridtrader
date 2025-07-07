Market Data
 1.0.0 
OAS3
Trader API - Market data

Contact Schwab Trader API team
Servers

https://api.schwabapi.com/marketdata/v1
Quotes
Get Quotes Web Service.



GET
/quotes
Get Quotes by list of symbols.


GET
/{symbol_id}/quotes
Get Quote by single symbol.

Option Chains
Get Option Chains Web Service.



GET
/chains
Get option chain for an optionable Symbol

Option Expiration Chain
Get Option Expiration Chain Web Service.



GET
/expirationchain
Get option expiration chain for an optionable symbol

PriceHistory
Get Price History Web Service.



GET
/pricehistory
Get PriceHistory for a single symbol and date ranges.

Movers
Get Movers Web Service.



GET
/movers/{symbol_id}
Get Movers for a specific index.

MarketHours
Get MarketHours Web Service.



GET
/markets
Get Market Hours for different markets.


GET
/markets/{market_id}
Get Market Hours for a single market.

Instruments
Get Instruments Web Service.



GET
/instruments
Get Instruments by symbols and projections.


GET
/instruments/{cusip_id}
Get Instrument by specific cusip


Schemas
Bond{
cusip	[...]
symbol	[...]
description	[...]
exchange	[...]
assetType	[...]
bondFactor	[...]
bondMultiplier	[...]
bondPrice	[...]
type	[...]
}
FundamentalInst{
symbol	[...]
high52	[...]
low52	[...]
dividendAmount	[...]
dividendYield	[...]
dividendDate	[...]
peRatio	[...]
pegRatio	[...]
pbRatio	[...]
prRatio	[...]
pcfRatio	[...]
grossMarginTTM	[...]
grossMarginMRQ	[...]
netProfitMarginTTM	[...]
netProfitMarginMRQ	[...]
operatingMarginTTM	[...]
operatingMarginMRQ	[...]
returnOnEquity	[...]
returnOnAssets	[...]
returnOnInvestment	[...]
quickRatio	[...]
currentRatio	[...]
interestCoverage	[...]
totalDebtToCapital	[...]
ltDebtToEquity	[...]
totalDebtToEquity	[...]
epsTTM	[...]
epsChangePercentTTM	[...]
epsChangeYear	[...]
epsChange	[...]
revChangeYear	[...]
revChangeTTM	[...]
revChangeIn	[...]
sharesOutstanding	[...]
marketCapFloat	[...]
marketCap	[...]
bookValuePerShare	[...]
shortIntToFloat	[...]
shortIntDayToCover	[...]
divGrowthRate3Year	[...]
dividendPayAmount	[...]
dividendPayDate	[...]
beta	[...]
vol1DayAvg	[...]
vol10DayAvg	[...]
vol3MonthAvg	[...]
avg10DaysVolume	[...]
avg1DayVolume	[...]
avg3MonthVolume	[...]
declarationDate	[...]
dividendFreq	[...]
eps	[...]
corpactionDate	[...]
dtnVolume	[...]
nextDividendPayDate	[...]
nextDividendDate	[...]
fundLeverageFactor	[...]
fundStrategy	[...]
}
Instrument{
cusip	[...]
symbol	[...]
description	[...]
exchange	[...]
assetType	[...]
type	[...]
}
InstrumentResponse{
cusip	[...]
symbol	[...]
description	[...]
exchange	[...]
assetType	[...]
bondFactor	[...]
bondMultiplier	[...]
bondPrice	[...]
fundamental	FundamentalInst{...}
instrumentInfo	Instrument{...}
bondInstrumentInfo	Bond{...}
type	[...]
}
Hours{
date	[...]
marketType	[...]
exchange	[...]
category	[...]
product	[...]
productName	[...]
isOpen	[...]
sessionHours	{...}
}
Interval{
start	[...]
end	[...]
}
Screener{
description:	
Security info of most moved with in an index

change	[...]
description	[...]
direction	[...]
last	[...]
symbol	[...]
totalVolume	[...]
}
Candle{
close	[...]
datetime	[...]
datetimeISO8601	[...]
high	[...]
low	[...]
open	[...]
volume	[...]
}
CandleList{
candles	[...]
empty	[...]
previousClose	[...]
previousCloseDate	[...]
previousCloseDateISO8601	[...]
symbol	[...]
}
EquityResponse{
description:	
Quote info of Equity security

assetMainType	AssetMainType[...]
assetSubType	EquityAssetSubType[...]
ssid	[...]
symbol	[...]
realtime	[...]
quoteType	QuoteType[...]
extended	ExtendedMarket{...}
fundamental	Fundamental{...}
quote	QuoteEquity{...}
reference	ReferenceEquity{...}
regular	RegularMarket{...}
}
QuoteError{
description:	
Partial or Custom errors per request

invalidCusips	[...]
invalidSSIDs	[...]
invalidSymbols	[...]
}
ExtendedMarket{
description:	
Quote data for extended hours

askPrice	[...]
askSize	[...]
bidPrice	[...]
bidSize	[...]
lastPrice	[...]
lastSize	[...]
mark	[...]
quoteTime	[...]
totalVolume	[...]
tradeTime	[...]
}
ForexResponse{
description:	
Quote info of Forex security

assetMainType	AssetMainType[...]
ssid	[...]
symbol	[...]
realtime	[...]
quote	QuoteForex{...}
reference	ReferenceForex{...}
}
Fundamental{
description:	
Fundamentals of a security

avg10DaysVolume	[...]
avg1YearVolume	[...]
declarationDate	[...]
divAmount	[...]
divExDate	[...]
divFreq	DivFreq[...]
divPayAmount	[...]
divPayDate	[...]
divYield	[...]
eps	[...]
fundLeverageFactor	[...]
fundStrategy	FundStrategy[...]
nextDivExDate	[...]
nextDivPayDate	[...]
peRatio	[...]
}
FutureOptionResponse{
description:	
Quote info of Future Option security

assetMainType	AssetMainType[...]
ssid	[...]
symbol	[...]
realtime	[...]
quote	QuoteFutureOption{...}
reference	ReferenceFutureOption{...}
}
FutureResponse{
description:	
Quote info of Future security

assetMainType	AssetMainType[...]
ssid	[...]
symbol	[...]
realtime	[...]
quote	QuoteFuture{...}
reference	ReferenceFuture{...}
}
IndexResponse{
description:	
Quote info of Index security

assetMainType	AssetMainType[...]
ssid	[...]
symbol	[...]
realtime	[...]
quote	QuoteIndex{...}
reference	ReferenceIndex{...}
}
MutualFundResponse{
description:	
Quote info of MutualFund security

assetMainType	AssetMainType[...]
assetSubType	MutualFundAssetSubType[...]
ssid	[...]
symbol	[...]
realtime	[...]
fundamental	Fundamental{...}
quote	QuoteMutualFund{...}
reference	ReferenceMutualFund{...}
}
OptionResponse{
description:	
Quote info of Option security

assetMainType	AssetMainType[...]
ssid	[...]
symbol	[...]
realtime	[...]
quote	QuoteOption{...}
reference	ReferenceOption{...}
}
QuoteEquity{
description:	
Quote data of Equity security

52WeekHigh	[...]
52WeekLow	[...]
askMICId	[...]
askPrice	[...]
askSize	[...]
askTime	[...]
bidMICId	[...]
bidPrice	[...]
bidSize	[...]
bidTime	[...]
closePrice	[...]
highPrice	[...]
lastMICId	[...]
lastPrice	[...]
lastSize	[...]
lowPrice	[...]
mark	[...]
markChange	[...]
markPercentChange	[...]
netChange	[...]
netPercentChange	[...]
openPrice	[...]
quoteTime	[...]
securityStatus	[...]
totalVolume	[...]
tradeTime	[...]
volatility	[...]
}
QuoteForex{
description:	
Quote data of Forex security

52WeekHigh	[...]
52WeekLow	[...]
askPrice	[...]
askSize	[...]
bidPrice	[...]
bidSize	[...]
closePrice	[...]
highPrice	[...]
lastPrice	[...]
lastSize	[...]
lowPrice	[...]
mark	[...]
netChange	[...]
netPercentChange	[...]
openPrice	[...]
quoteTime	[...]
securityStatus	[...]
tick	[...]
tickAmount	[...]
totalVolume	[...]
tradeTime	[...]
}
QuoteFuture{
description:	
Quote data of Future security

askMICId	[...]
askPrice	[...]
askSize	[...]
askTime	[...]
bidMICId	[...]
bidPrice	[...]
bidSize	[...]
bidTime	[...]
closePrice	[...]
futurePercentChange	[...]
highPrice	[...]
lastMICId	[...]
lastPrice	[...]
lastSize	[...]
lowPrice	[...]
mark	[...]
netChange	[...]
openInterest	[...]
openPrice	[...]
quoteTime	[...]
quotedInSession	[...]
securityStatus	[...]
settleTime	[...]
tick	[...]
tickAmount	[...]
totalVolume	[...]
tradeTime	[...]
}
QuoteFutureOption{
description:	
Quote data of Option security

askMICId	[...]
askPrice	[...]
askSize	[...]
bidMICId	[...]
bidPrice	[...]
bidSize	[...]
closePrice	[...]
highPrice	[...]
lastMICId	[...]
lastPrice	[...]
lastSize	[...]
lowPrice	[...]
mark	[...]
markChange	[...]
netChange	[...]
netPercentChange	[...]
openInterest	[...]
openPrice	[...]
quoteTime	[...]
securityStatus	[...]
settlemetPrice	[...]
tick	[...]
tickAmount	[...]
totalVolume	[...]
tradeTime	[...]
}
QuoteIndex{
description:	
Quote data of Index security

52WeekHigh	[...]
52WeekLow	[...]
closePrice	[...]
highPrice	[...]
lastPrice	[...]
lowPrice	[...]
netChange	[...]
netPercentChange	[...]
openPrice	[...]
securityStatus	[...]
totalVolume	[...]
tradeTime	[...]
}
QuoteMutualFund{
description:	
Quote data of Mutual Fund security

52WeekHigh	[...]
52WeekLow	[...]
closePrice	[...]
nAV	[...]
netChange	[...]
netPercentChange	[...]
securityStatus	[...]
totalVolume	[...]
tradeTime	[...]
}
QuoteOption{
description:	
Quote data of Option security

52WeekHigh	[...]
52WeekLow	[...]
askPrice	[...]
askSize	[...]
bidPrice	[...]
bidSize	[...]
closePrice	[...]
delta	[...]
gamma	[...]
highPrice	[...]
indAskPrice	[...]
indBidPrice	[...]
indQuoteTime	[...]
impliedYield	[...]
lastPrice	[...]
lastSize	[...]
lowPrice	[...]
mark	[...]
markChange	[...]
markPercentChange	[...]
moneyIntrinsicValue	[...]
netChange	[...]
netPercentChange	[...]
openInterest	[...]
openPrice	[...]
quoteTime	[...]
rho	[...]
securityStatus	[...]
theoreticalOptionValue	[...]
theta	[...]
timeValue	[...]
totalVolume	[...]
tradeTime	[...]
underlyingPrice	[...]
vega	[...]
volatility	[...]
}
QuoteRequest{
description:	
Request one or more quote data in POST body

cusips	[...]
fields	[...]
ssids	[...]
symbols	[...]
realtime	[...]
indicative	[...]
}
QuoteResponse{
description:	
a (symbol, QuoteResponse) map. SCHWis an example key

< * >:	QuoteResponseObject{...}
}
QuoteResponseObject{
oneOf ->	
EquityResponse{...}
OptionResponse{...}
ForexResponse{...}
FutureResponse{...}
FutureOptionResponse{...}
IndexResponse{...}
MutualFundResponse{...}
QuoteError{...}
}
ReferenceEquity{
description:	
Reference data of Equity security

cusip	[...]
description	[...]
exchange	[...]
exchangeName	[...]
fsiDesc	[...]
htbQuantity	[...]
htbRate	[...]
isHardToBorrow	[...]
isShortable	[...]
otcMarketTier	[...]
}
ReferenceForex{
description:	
Reference data of Forex security

description	[...]
exchange	[...]
exchangeName	[...]
isTradable	[...]
marketMaker	[...]
product	[...]
tradingHours	[...]
}
ReferenceFuture{
description:	
Reference data of Future security

description	[...]
exchange	[...]
exchangeName	[...]
futureActiveSymbol	[...]
futureExpirationDate	[...]
futureIsActive	[...]
futureMultiplier	[...]
futurePriceFormat	[...]
futureSettlementPrice	[...]
futureTradingHours	[...]
product	[...]
}
ReferenceFutureOption{
description:	
Reference data of Future Option security

contractType	ContractType[...]
description	[...]
exchange	[...]
exchangeName	[...]
multiplier	[...]
expirationDate	[...]
expirationStyle	[...]
strikePrice	[...]
underlying	[...]
}
ReferenceIndex{
description:	
Reference data of Index security

description	[...]
exchange	[...]
exchangeName	[...]
}
ReferenceMutualFund{
description:	
Reference data of MutualFund security

cusip	[...]
description	[...]
exchange	[...]
exchangeName	[...]
}
ReferenceOption{
description:	
Reference data of Option security

contractType	ContractType[...]
cusip	[...]
daysToExpiration	[...]
deliverables	[...]
description	[...]
exchange	[...]
exchangeName	[...]
exerciseType	ExerciseType[...]
expirationDay	[...]
expirationMonth	[...]
expirationType	ExpirationType[...]
expirationYear	[...]
isPennyPilot	[...]
lastTradingDay	[...]
multiplier	[...]
settlementType	SettlementType[...]
strikePrice	[...]
underlying	[...]
}
RegularMarket{
description:	
Market info of security

regularMarketLastPrice	[...]
regularMarketLastSize	[...]
regularMarketNetChange	[...]
regularMarketPercentChange	[...]
regularMarketTradeTime	[...]
}
AssetMainTypestring
Instrument's asset type

Enum:
Array [ 8 ]
EquityAssetSubTypestring
nullable: true
Asset Sub Type (only there if applicable)

Enum:
Array [ 11 ]
MutualFundAssetSubTypestring
nullable: true
Asset Sub Type (only there if applicable)

Enum:
Array [ 4 ]
ContractTypestring
Indicates call or put

Enum:
Array [ 2 ]
SettlementTypestring
option contract settlement type AM or PM

Enum:
Array [ 2 ]
ExpirationTypestring
M for End Of Month Expiration Calendar Cycle. (To match the last business day of the month), Q for Quarterly expirations (last business day of the quarter month MAR/JUN/SEP/DEC), W for Weekly expiration (also called Friday Short Term Expirations) and S for Expires 3rd Friday of the month (also known as regular options).

Enum:
Array [ 4 ]
FundStrategystring
nullable: true
FundStrategy "A" - Active "L" - Leveraged "P" - Passive "Q" - Quantitative "S" - Short

Enum:
Array [ 6 ]
ExerciseTypestring
option contract exercise type America or European

Enum:
Array [ 2 ]
DivFreqinteger
nullable: true
Dividend frequency 1 – once a year or annually 2 – 2x a year or semi-annualy 3 - 3x a year (ex. ARCO, EBRPF) 4 – 4x a year or quarterly 6 - 6x per yr or every other month 11 – 11x a year (ex. FBND, FCOR) 12 – 12x a year or monthly

Enum:
Array [ 8 ]
QuoteTypestring
nullable: true
NBBO - realtime, NFL - Non-fee liable quote.

Enum:
Array [ 3 ]
ErrorResponse{
errors	[...]
}
Error{
id	[...]
status	[...]
title	[...]
detail	[...]
source	ErrorSource{...}
}
ErrorSource{
description:	
Who is responsible for triggering these errors.

pointer	[...]
parameter	[...]
header	[...]
}
OptionChain{
symbol	[...]
status	[...]
underlying	Underlying{...}
strategy	[...]
interval	[...]
isDelayed	[...]
isIndex	[...]
daysToExpiration	[...]
interestRate	[...]
underlyingPrice	[...]
volatility	[...]
callExpDateMap	{...}
putExpDateMap	{...}
}
OptionContractMap{
< * >:	OptionContract{...}
}
Underlying{
ask	[...]
askSize	[...]
bid	[...]
bidSize	[...]
change	[...]
close	[...]
delayed	[...]
description	[...]
exchangeName	[...]
fiftyTwoWeekHigh	[...]
fiftyTwoWeekLow	[...]
highPrice	[...]
last	[...]
lowPrice	[...]
mark	[...]
markChange	[...]
markPercentChange	[...]
openPrice	[...]
percentChange	[...]
quoteTime	[...]
symbol	[...]
totalVolume	[...]
tradeTime	[...]
}
OptionDeliverables{
symbol	[...]
assetType	[...]
deliverableUnits	[...]
currencyType	[...]
}
OptionContract{
putCall	[...]
symbol	[...]
description	[...]
exchangeName	[...]
bidPrice	[...]
askPrice	[...]
lastPrice	[...]
markPrice	[...]
bidSize	[...]
askSize	[...]
lastSize	[...]
highPrice	[...]
lowPrice	[...]
openPrice	[...]
closePrice	[...]
totalVolume	[...]
tradeDate	[...]
quoteTimeInLong	[...]
tradeTimeInLong	[...]
netChange	[...]
volatility	[...]
delta	[...]
gamma	[...]
theta	[...]
vega	[...]
rho	[...]
timeValue	[...]
openInterest	[...]
isInTheMoney	[...]
theoreticalOptionValue	[...]
theoreticalVolatility	[...]
isMini	[...]
isNonStandard	[...]
optionDeliverablesList	[...]
strikePrice	[...]
expirationDate	[...]
daysToExpiration	[...]
expirationType	ExpirationType[...]
lastTradingDay	[...]
multiplier	[...]
settlementType	SettlementType[...]
deliverableNote	[...]
isIndexOption	[...]
percentChange	[...]
markChange	[...]
markPercentChange	[...]
isPennyPilot	[...]
intrinsicValue	[...]
optionRoot	[...]
}
ExpirationChain{
status	[...]
expirationList	[...]
}
Expiration{
description:	
expiration type

daysToExpiration	[...]
expiration	[...]
expirationType	ExpirationType[...]
standard	[...]
settlementType	SettlementType[...]
optionRoots	[...]
}
