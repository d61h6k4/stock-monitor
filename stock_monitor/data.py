from stock_monitor.models import Stock, Arbitrage, Expectation
from datetime import datetime, timezone


def vix_stocks(period: str, interval: str):
    return [Stock(ticker_name, period=period, interval=interval) for ticker_name in
            ["GOOG", "NVDA", "ASML", "KLAC", "WAF.DE", "MSFT"]]


def tax_loss_jan_stocks(period: str, interval: str):
    return [Stock("SLGC", period=period, interval=interval,
                  description=r"""Somalogic \$SLGC, \$2.26 - A leading platform for proteomics analysis,
                                  \$SLGC has a \$435 mm cap w/ \$550 mm+ of cash. \$SLGC has cut costs and
                                  should burn ~\$80-\$100 mm in '23, w/ a partnership with \$ILMN due to
                                  launch in '24.  New Exec Chair seems like validation."""),
            Stock("ALLT", period=period, interval=interval,
                  description=r"""Allot \$ALLT, \$2.86 - A provider of carrier networking solutions,
                                  \$ALLT's move into a new consumer facing security biz has been a disaster.
                                  Mgmt, however, now appears under pressure to rollback that effort.
                                  Core DPI biz is very strong. \$110 mm cap with good balance sheet."""),
            Stock("ACTG", period=period, interval=interval,
                  description=r"""Acacia \$ACTG, \$3.59 - Stock now trades at 68% of \$5.25 per share book
                                  value pro-forma for Starboard deal, and Viamet and Wifi 6 patents are
                                  probably worth \$1+ more per share. Balance sheet is rock solid and loaded
                                  with cash, & $ACTG has bought back a lot of stock in past."""),
            Stock("DSP", period=period, interval=interval,
                  description=r"""Viant \$DSP, \$3.34 - Trading flat with its ~\$225 mm of cash w/ breakeven
                                  operations (w/ solid EBITDA in past), \$DSP offers a buy side programmatic
                                  ad-tech platform that has nicely grown ad spend volume over the years.
                                  The two brothers who control \$DSP are solid entrepreneurs"""),
            Stock("CGNT", period=period, interval=interval,
                  description=r"""Cognyte \$CGNT, \$2.40 - This cybersecurity play had a rocky year of
                                  operations but appears to be regaining its footing with cost cuts and asset sales.
                                  Biz has been profitable in past and balance sheet is now on firmer ground.
                                  \$160 mm cap."""),
            ]


def ideas(period: str, interval: str):
    ideas = [Stock("VONOY", period=period, interval=interval,
                   expectation=Expectation(price=30, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Germany's biggest landlord $VNA is priced at a 70% discount to its net asset value.
                                  Its share price would need to 3x just to reach its net asset value.
                                  [Source](https://twitter.com/askjussi/status/1611358663754813440)"""),
             Stock("DBRG", period=period, interval=interval,
                   expectation=Expectation(price=40, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Pure play alternative asset manager focused exclusively on network infrastructure
                                  investments. A transformed Colony Capital with nearly all legacy assets sold off.
                                  Significant step up in earnings expected in 2023 after the launch of several new
                                  funds. Market is pricing in zero success in fundraising and gives no credit for the
                                  carried interest. Sentiment is likely to reverse upon successful new fund launches.
                                  Insiders started buying stock recently. Infrastructure is a key growth engine for
                                  alternative asset managers. \$KKR, \$BX, etc., are all raising significant capital
                                  for infrastructure investments and \$DBRG is the fastest-growing manager out there.
                                  Valuing fee-related earnings at 22x, results in a SOTP valuation of \$32\/share with an
                                  additional \$5\/share from carried interest.
                                  **Exp. gain: +200\% to \$40\/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)"""),
             Stock("CRNT", period=period, interval=interval,
                   expectation=Expectation(price=3.08, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""Vendor for global wireless network operators specializing in backhaul solutions.
                                  Shareholders have recently rejected a hostile takeover by peer \$AVNW at \$3.8/share.
                                  Renewed talks between AVNW and CRNT present the potential for near-term upside
                                  realization. While \$AVNW is the leader in NA backhaul, CRNT is now encroaching on
                                  its territory, having secured contracts with every NA Tier 1 operator. AVNW used a
                                  difficult equity market environment to try to opportunistically scoop up an
                                  undervalued asset.Post proxy fight CRNT management is forced to drive shareholder
                                  value.Trades near its historical 1x book value floor. Failed takeover attempt at
                                  \$3.08/share in Aug’22. Management’s internal value estimate of \$5/share.
                                  **Exp. gain: +70% to\$3.08+**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)"""),
             Stock("SI", period=period, interval=interval,
                   expectation=Expectation(price=120, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""FDIC-regulated bank which specializes in serving the crypto-currency ecosystem and
                                  acquired the Diem platform from \$META. An institution with a very liquid asset book
                                  of government securities trading below tangible book. No credit risk exposure to
                                  crypto.The stock is down from \$220 to \$30 over the past year. At 1xBV, the downside
                                  is very well protected with material optionality from crypto recovery or Diem getting
                                  regulatory approval.Trades at 1xBV. In an upside scenario, it is a differentiated
                                  financial institution worth several multiples of BV. If Diem takes off \$SI becomes a
                                  high-growth technology company.
                                  **Exp. gain: 2x-4x.**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)"""),
             Stock("AMKR", period=period, interval=interval,
                   expectation=Expectation(price=87, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Semiconductor assembly services provider – the world’s most wonderfully boring
                                  businesses to own. At 9x earnings and shifting into higher margin services.
                                  For a semi business, it has very low cyclicality and low capex needs, and yet is
                                  delivering above-industry revenue growth with 3 year CAGR of 20%. Oligopolistic
                                  industry – AMKR is the No.2 player with a 25% share, behind \$ASX with 35%. Due to
                                  increasing chip complexity, the industry is shifting towards less commoditized and
                                  more advanced packaging/assembly solutions, requiring more R&D and tighter
                                  integration with customers. This also drives increasing margins for key players.
                                  Should trade at an above-market multiple of 20x vs 9x today. ’23 and ’24 EPS are
                                  expected at \$3 and \$4. Easy double with \$4 fwd EPS and 10.5x multiple. DCF model
                                  results in \$87/share. **Exp. gain: +100% by 2H23.**
                                  [Source.](https://twitter.com/InvestSpecial/status/1612025171879010305)"""),
             Stock("XMTR", period=period, interval=interval,
                   expectation=Expectation(price=45, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Marketplace for small batch manufacturing and prototyping. Currently trades at its
                                  Jun’21 IPO level and at 4.5x revenue, while comps are in the 1-2x range. Competitive 
                                  and low-entry barrier industry that is significantly exposed to macro headwinds. 
                                  Clients and suppliers can as easily connect directly. 
                                  No clear operating leverage with increasing scale. Relies heavily on Google Adwords 
                                  to drive traffic. Guidedown in pricing already happened with Q3’22 results, 
                                  volume might drop in 2023.Trades at 4.5x revenues, still at the IPO price vs. a comp 
                                  universe 3-D printers and short-run fabricators in the 1-2x range. **Exp. gain: 50%-75%**
                                  [Source.](https://twitter.com/InvestSpecial/status/1612387567302840320)"""),
             Stock("FIP", period=period, interval=interval,
                   expectation=Expectation(price=7, date=datetime(2023, 6, 1, tzinfo=timezone.utc)),
                   description=r"""Recent spin-off from \$FTAI with 4 infrastructure assets: 3 energy terminals and a
                                  railroad business. EBITDA is set to increase from \$140m today to \$250m in the next
                                  12-18 months. FPI’s Jefferson terminal is now on cusp of generating strong earnings.
                                  Transtar railroad earnings have been consistently increasing through new business
                                  initiatives. Construction of the 485MW power plant at Long Ridge is complete.
                                  Downside is well protected at current share price levels.Base case EBITDA is set to
                                  grow from \$140 million today to \$250 million over the next 12-18 months.
                                  At 11x multiple, the target of \$6.7/share. **Exp. gain: +130% to \$7/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)"""),
             Stock("ALIT", period=period, interval=interval,
                   expectation=Expectation(price=11, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""Provider of outsourced human capital management services/software with multiple
                                  upcoming event catalysts. Steady business, with 3-5 year contracts, 15-year average
                                  customer life, and 97% rev retention. Comp set is performing very well in the stock
                                  market.Stock was down 20% after a botched secondary offering. However, Bill Foley
                                  pulled out from selling. His lack of participation in the secondary was extremely
                                  telling. His number two, Rick Massey, subsequently bought \$840k of stock around
                                  current levelsPeers \$WTW and \$G with similar expected growth and financial profiles
                                  trade at 11x-11.5x 1-year forward EBITDA.
                                  At this multiple \$ALIT is worth \$10.5-11.0/share today.
                                  **Exp. gain: +20% to \$11/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)"""),
             Stock("ZIMV", period=period, interval=interval,
                   expectation=Expectation(price=37, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Recent spin-off from Zimmer Biomet with shares down 80% from the first day of trading.
                                  Orthopedics company offering spine surgery solutions and dental implants. Stable,
                                  65% GM business, set to benefit from post-pandemic recovery in elective surgeries.
                                  Margin improvement potential from the current 9% to 15-20% peer levels. Trades far
                                  below peer group on a revenue multiple. Trailing revenues were weak due to distortion
                                  by several transitory factors.Current EV/Sales of 0.75x is far below the peer group’s
                                  3.3x. Full-recovery EV/EBIT of around 7x vs around 15x for the peer group.
                                  At 15x multiple would be valued at \$37/share. **Exp. gain: +300% to \$37/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)"""),
             Stock("BJ", period=period, interval=interval,
                   expectation=Expectation(price=140, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""**What does BJ do?** The business is a discount wholesale club like Costco but
                                   focused on a more middle-class income demographic (Costco tends to skew higher
                                   income). BJ’s charges an annual membership fee of \$55 to \$110 and delivers
                                   extreme savings of 30% on average compared to traditional grocery and general
                                   merchandise stores. This is a strong value proposition for a family that shops
                                   once or twice per month for household essentials.
                                   **Why is it a good bet?** Discount retailers tend to outperform during
                                   recessionary periods as well as inflationary periods when consumers are looking
                                   for bargains. During the 2008/2009 recession, discounters such as Dollar General
                                   posted strong sales comps. We studied several discount retail concepts this summer
                                   and determined that BJ’s presents the best longterm opportunity
                                   **Why does the opportunity exist?** With just 226 store units compared to Costco’s
                                   847 units, BJ’s has a significant opportunity to grow its store base and is
                                   currently accelerating new unit openings
                                   **What’s the prize if you’re right?** Investors appreciate the quality of the
                                   wholesale club model and have awarded Costco a 32x price-to-earnings multiple.
                                   Despite BJ’s being a ‘Costco clone’, its stock only trades for 17.5x earnings –
                                   a near 50% discount(!). [Source](https://macro-ops.com)"""),
             Stock("HLS.TO", period=period, interval=interval,
                   expectation=Expectation(price=25, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""Small cap Canadian pharma with shares near all-time lows and business fundamentals
                                   finally inflecting to the positive. Investment case is mainly based on one of two
                                   HLS’s drugs, Vascepa, that is in the initial stages of commercialization.
                                   Vascepa is approved, clinically effective, and has reimbursement coverage
                                   Pfizer Canada is the team pushing things forward for commercialization
                                   Sales are growing 30%-40% QoQ and are only now approaching sufficient prescription
                                   levels to break evenThe initial Vascepa commercialization difficulties were mainly
                                   caused by Canada’s lengthy COVID lockdown.
                                   Precedent drugs suggest management's estimate of 10% penetration is overly conservative
                                   and that 20-40% levels could be reached.The already commercialized drug Clozaril alone
                                   supports current HLS valuation, implying less than zero value for Vascepa.
                                   With Vascepa roll-out, HLS is worth \$25/share.
                                   **Exp. gain: +150% to \$25/share.**.
                                   [Source](https://twitter.com/InvestSpecial/status/1615303074473451521)"""),
             Stock("TCMD", period=period, interval=interval,
                   expectation=Expectation(price=17, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Meditech company with two products for treating underserved chronic conditions at home.
                                   Flexitouch for lymphedema and Afflovest for bronchiectasis/fibrosis. Currently,
                                   TCMD is underearning as investment in Flexitouch salesforce havs't yet paid off due
                                   to covid. The sales of the second product (Afflovest, acquired in Sep’21) are still
                                   ramping up, but eventually, 50-60% of incremental revenue should drop down to EBIT.
                                   The market for Afflovest remains very large and underpenetrated.– Demand has been so
                                   great thus far in 2022 – the company not only increased revenue guidance for
                                   Afflovest from \$20m to \$35m (100% yoy growth) but also had to sign on a second
                                   source supplier to be able to meet the demand.– Assuming Afflovest sales of \$70m
                                   by '25, it would do ~\$25m of EBITDA with little capex requirements vs. current EV of \$230m.
                                   Remaining \$208m of Flexitouch sales come free.
                                   **Exp. gain: +70% to \$17/share in two years.**
                                   [Source](https://twitter.com/InvestSpecial/status/1617847238239076353)"""),
             Stock("APD", period=period, interval=interval,
                   expectation=Expectation(price=600, date=datetime(2027, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Large-cap producer of atmospheric and industrial gases (oxygen, nitrogen, hydrogen
                                   and etc). APD is in a great position to take advantage of the hydrogen future, and
                                   they have been the most aggressive of their peers in going after the opportunity.
                                   Expected high-teens IRR over the next 5 year, potentially above this range if
                                   hydrogen plays out as hoped. 52% of revenue is supplied on-customer-site with
                                   15-20 year contracts, while the rest comes from merchant channels typically under
                                   3-5y contracts. Stable cash flows with proven ability to pass through commodity
                                   cost increases. 50% of earnings paid out as dividends (2% yield).
                                   An oligopolistic industry that has historically provided stability and pricing power.
                                   Trades roughly in line with historical multiples at 28x fwd PE. Investors are not
                                   paying much for the tremendous optionality around hydrogen, gasification, and carbon
                                   capture. **Exp. gain: +100% to $600/share in 5 years.**
                                   [Source](https://twitter.com/InvestSpecial/status/1618241155103064071)"""),
             Stock("ALGN", period=period, interval=interval,
                   expectation=Expectation(price=120, date=datetime(2023, 6, 30, tzinfo=timezone.utc)),
                   description=r"""Producer of Invisalign clear teeth aligners. Invented and won the category,
                                   crushed the competition – 75% market share. However, the market does not appreciate
                                   how much the demand was pulled forward during COVID. Has grown 20-25% during
                                   2010-2019, but then growth exploded to 50-60% in 2021. Channel checks indicate
                                   prescribers of Invisalign are seeing a slowdown in their business, with the 2022
                                   year expected to be down 10% vs 2019 levels. Given that treatment times are 6-18
                                   months in length, this slowdown is not yet fully visible in ALGN numbers, but
                                   inventory is increasing and deferred revenue growth is decelerating. 2023 earnings
                                   are set to decline from \$8/share today to closer to \$6/share.
                                   At 20-25x PE, the target is \$120-\$150/share.
                                   **Exp. gain: 20-40% to \$120-\$150/share.**
                                   [Source](https://twitter.com/InvestSpecial/status/1620009107309699072)"""),
             Stock("CAL", period=period, interval=interval,
                   expectation=Expectation(price=40, date=datetime(2023, 6, 30, tzinfo=timezone.utc)),
                   description=r"""Diversified footwear retailer at 5x PE. Owns the Famous Footwear brand of stores
                                   (870 stores). Equity is materially mispriced and generates significant free cash
                                   flow. Q4 results are expected to be nicely above guidance as a normal seasonal
                                   pattern recovers into Christmas. Set to fully repay its debt over the next 18 months.
                                   Repurchased 7% of shares over last 3 quarters and has large remaining repo
                                   authorization. Significant upside if CAL trades up to the mean of non-growth shoe
                                   retailers. At PE of 7x-8x 2023, would be \$40 stock.
                                   **Exp. gain: +85% to \$40/share.**
                                   [Source](https://twitter.com/InvestSpecial/status/1620009107309699072)"""),
             Stock("MIR", period=period, interval=interval,
                   expectation=Expectation(price=10, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Industry leader in mission-critical radiation measuring devices and services.
                                   40-60% market share in the markets it participates. Has been beaten down
                                   mainly due to quarterly guidance misses from component shortages and canceled
                                   projects due to the Ukraine. SPAC provenance, poor execution, and its terrible
                                   public market performance have led investors to trade it like a low-quality
                                   industrial business. MIR’s acyclicality, market position, and margins argue for
                                   a better multiple. Expected to revert to normalized earnings after the
                                   aforementioned temporary pressures ease. The elevated order book indicates
                                   positive exposure to secular growth in nuclear power.Trades at 11x E2023 EBITDA
                                   of \$193m. Higher quality industrial peers trade at 15-25x EV/EBITDA.
                                   Mirion should at least reach the low-end of this range implying a
                                   \$10/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1623987849052692482)"""),
             Stock("BALL", period=period, interval=interval,
                   expectation=Expectation(price=70, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Beverage can producer with a 30% market share globally and 40% in the US.
                                   Primary customers are companies like \$BUD and \$KO. Stock sold off due to
                                   a combination of post-covid oversupply in the beverage can industry, increased
                                   aluminum prices, and moderating consumer demand. Operating margins contracted
                                   from 13% in 2020 to 10% in 2022.These factors are expected to unwind in 2023
                                   setting up the perfect storm for BALL. The supply/demand disbalance is expected
                                   to normalize in 2023, while decreases in aluminum prices are expected to bring margins
                                   to historical levels. EPS is expected to reach \$3.5/share in 2023 (7% above consensus).
                                   Historical 20x multiple implies a \$70/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1627623767869386752)"""),
             Stock("MATV", period=period, interval=interval,
                   expectation=Expectation(price=32, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Specialty materials business formed in 2022 as a result of merger with significant synergies.
                                   Good business with cyclically depressed EBITDA. Should be a ~MSD revenue grower and approaching
                                   high-teen EBITDA margins with low capex intensity (~3% of revenue).Extremely cheap trading 6.6x
                                   management’s EBITDA target. Good FCF generator with a 14% 2023 levered FCF yield. Expected to
                                   divest certain businesses to crystallize value. Last year insiders purchased nearly \$6mm in
                                   stock at an average price of \$23.5. Currently trading at 6.6x management’s \$450mm EBITDA target.
                                   On SOTP basis, with 10-12x EBITDA on ATS segment and 5-6x on the FBS segment, price target of
                                   \$32-43/share.
                                   [Source](https://twitter.com/InvestSpecial/status/1627984064601894915)"""),
             Stock("NTDOY", period=period, interval=interval,
                   expectation=Expectation(price=30, date=datetime(2027, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Nintendo today offers a robust 3x upside to reach intrinsic value estimate of ~\$110bn EV.
                                   The market is massively mispricing Nintendo’s “App Store Platform” or third-party software
                                   business.Nintendo Switch is a thriving distribution channel that has already attracted a large
                                   thriving ecosystem of third-party games. This marks a major strategic shift in how Nintendo views
                                   its console business.As a result, Software sales have inflected in recent years, overtaking
                                   hardware for the first time in 2022. Primed for continued massive margin expansion, from already
                                   improved ~35% to 50%, based on reasonable extrapolations of the present trends.Game seg.
                                   is worth \$65bn on \$12bn fwd. rev, 33% EBIT margin and 23x NOPAT
                                   App Store Platform is worth \$45bn on \$3.5bn FY27 rev, 87% margin and 30x NOPAT
                                   Suming up to \$110bn vs \$37bn EV today.
                                   [Source](https://twitter.com/InvestSpecial/status/1629419792699383808)."""),
             Stock("FTAI", period=period, interval=interval,
                   expectation=Expectation(price=94, date=datetime(2027, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Aircraft and engine lessor that has gone through a major transformation from a complex “mess”
                                   of assets to a pure-play aviation company. On the cusp of seeing substantial growth in its parts
                                   & service business and that should translate into a higher multiple. Product and services segment
                                   is set to contribute half of the profitability vs 15% currently. Trades materially below peers.
                                   Survived major setbacks of Covid and the Russia/Ukraine war with a number of aircrafts seized
                                   or destroyed. Recently spun-out infrastructure assets, which not only simplified and derisked the
                                   FTAI story but also improved the balance sheet. 6.3% dividend yield limits the downside.
                                   EBITDA set to grow from \$423m in 2022 to $1b in 2026. Multiple expected to expand from 9.7x today to 12x.
                                   Leasing peers trade at 10x ’23 EBITDA and product comps at 15x.
                                   [Source](https://twitter.com/InvestSpecial/status/1629419792699383808)"""),
             Stock("AE", period=period, interval=interval,
                   expectation=Expectation(price=120, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Transportation and logistics company serving the energy and chemical sectors, primarily onshore.
                                   Has momentum in each of its core business segments. Trades under 3x EBITDA.
                                   New management is turning the business around.Previously poorly managed for many years and run like
                                   a private company under Adams family control. In Nov’22 all 44% of the family’s ownership was cashed
                                   out at \$36/share. Current management team led by the current CEO was hired in 2018 to turn around
                                   operations. Despite the pandemic, since then the company has been meaningfully building adjusted FCF.
                                   Recently completed highly accretive acquisitions of Firebird Bulk Carriers and Phoenix Oil for about
                                   \$40m in cash. Repurchases and acquisitions, the net debt is close to zero. Expected to generate \$40m
                                   of adj. EBITDA in 2022 and \$50m+ in 2023. Trades at 3x 2022 adjusted EBITDA and 2.5x 2023 estimated
                                   adj. EBITDA. At 6x multiple would be worth $120/share."""),
             Stock("DSEY", period=period, interval=interval,
                   expectation=Expectation(price=9, date=datetime(2023, 6, 30, tzinfo=timezone.utc)),
                   description=r"""Diversey is a provider of cleaning products and services to institutional customers such as hospitals,
                                   hotels, and food and beverage producers. Stock is trading at a 50% discount from its Jan’22 levels due
                                   to the compression of margins and a strong USD. Headwinds are expected to turn into tailwinds as margins
                                   begin normalizing while the strong dollar seems to have topped. Plus DSEY operates a pretty sticky
                                   business and has a scale advantage over its peers usually the #1 or #2 player in most markets.
                                   Trades at 11x depressed 2022 EBITDA or 8x E2025 normalized EBITDA.
                                   At 10-12x EBITDA multiple, stock is worth \$9-12/share."""),
             Stock("BTI", period=period, interval=interval,
                   expectation=Expectation(price=58, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""British American Tabacco - at only 7.8x fwd earnings and nearing inflection point in terms of growth.
                                   At a lower valuation than during the worst of the GFC, and roughly in-line with COVID lows. As the company
                                   adds non-combustibles to their mix, margins should continue to move higher. The market is more willing to
                                   pay a premium multiple for a tobacco business with a larger % of non-smoking products in the portfolio
                                   (as happened with \$PM case). Inflation-proof non-cyclical stock with a stable 8% dividend yield.
                                   Together with EPS growth of 6-7% per year, BTI can be a 14-15% IRR stock for investors without rerating.
                                   That's before any EPS growth from non-combustibles. Bears point out that tobacco names will never trade
                                   at historical P/E multiples owing to heavy government regulation and the movement toward ESG investing.
                                   But the irony is that regulation only ensures that the supply side of the industry remains tight.BTI is
                                   expected to generate £4.26 of EPS in 2024. Historically traded at 12x EBITDA and 13x PE
                                   Re-rating to 10x 2024 eps results in a \$58/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1633420824442019842)"""),
             Stock("CZR", period=period, interval=interval,
                   expectation=Expectation(price=150, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""The largest gaming operator in the US with over 50 properties. 50% selloff from Oct'21 highs due to
                                   recession fears/risk aversion looks unwarranted as CZS offers a stable 15% FCF yield. Meanwhile,
                                   the downside looks protected by CZR’s owned real estate. Most importantly, there is the optionality
                                   of FCF expansion through normalization of growth CAPEX, interest expense reduction through debt repayments,
                                   and digital business inflection to profitability as it benefits from i-gaming growth.
                                   At 15x EBITDA (4x below average peer multiple over the last decade), the company would be valued at \$150/share.
                                   [Source](https://twitter.com/InvestSpecial/status/1633420824442019842)"""),
             Stock("WBA", period=period, interval=interval,
                   expectation=Expectation(price=70, date=datetime(2023, 8, 1, tzinfo=timezone.utc)),
                   description=r"""Wallgreens Boots Alliance - trades near all-time lows on virtually every metric. Fundamentals are
                                   expected to inflect in the second half of FY23. Company’s YOY EPS trajectory is projected to flip
                                   from about -31% in the first half, to 29% in the back-half. This will be driven by lower COVID headwinds,
                                   improvements in WBA’s Healthcare business, the timing of reimbursements, and lower COGS. The company has
                                   been transitioning under its new CEO into a multi-channel technology-driven healthcare provider and a
                                   one-stop shop for all healthcare needs. This is expected to drive longer-term EPS growth in the 13-15% range.
                                   Another catalyst is the potential sale of its large UK subsidiary Boots – rumors have been circulating
                                   that it might get sold at the right price. Trades at an 8.1x PE for 2023 and 7.3x for 2024.
                                   At historical discount levels (5-10%) would be \$70 stock.
                                   [Source](https://twitter.com/InvestSpecial/status/1634143032609046530)"""),
             ]

    def yield_per_day(x):
        y = (x.expectation.price - x.history.iloc[-1]["Open"]) / x.history.iloc[-1]["Open"] * 100.0
        d = (x.expectation.date - x.last_date).days
        return y / d

    return reversed(sorted(ideas, key=yield_per_day))


def stocks(period: str, interval: str):
    res = []
    for ticker_name in ["TGNA", "KOP", "CEG", "CNQ", "BABA"]:
        buy_date = None
        description = None
        if ticker_name == "TGNA":
            buy_date = datetime(2022, 12, 1, tzinfo=timezone.utc)
            description = "Arbitrage"
        elif ticker_name == "KOP":
            buy_date = datetime(2022, 12, 6, tzinfo=timezone.utc)
            description = """Koppers Holdings Inc. has three business segments: Railroad and Utility Products and
                             Services (RUPS), Performance Chemicals (PC) and Carbon Materials and Chemicals (CMC).
                             Basic materials, chemistry.
                             While waiting for recession.
                          """
        elif ticker_name == "CEG":
            buy_date = datetime(2022, 12, 6, tzinfo=timezone.utc)
            description = """Constellation Energy Corporation, formerly Constellation Newholdco, Inc., is a clean
                             energy company. The Company is focused on carbon-free electricity. It is a supplier
                             of clean energy and sustainable solutions to homes, businesses, public sector, community
                             aggregations and a range of wholesale customers, such as municipalities, cooperatives.
                             Utility, energy.
                             While waiting for recession.
                          """
        elif ticker_name == "CNQ":
            buy_date = datetime(2022, 12, 19, tzinfo=timezone.utc)
            description = """Canadian Natural Resources Limited is an independent crude oil and natural gas exploration,
                             development and production company.
                             Energy, oil & gas.
                             War in Ukraine and sanctions on the Russia.
                          """
        elif ticker_name == "BABA":
            buy_date = datetime(2023, 3, 6, tzinfo=timezone.utc)
            description = r"""Alibaba Group Holding Limited.
                              Bet on China reopening, Alibaba is Consumer Cyclical, so should benefit from reopening.
                           """
        assert buy_date is not None
        assert description is not None
        res.append(Stock(ticker_name, period=period, interval=interval, buy_date=buy_date, description=description))
    return res


def arbitrages(period: str):
    res = [Arbitrage(target=Stock(ticker_name="ATVI", period=period), buyer=Stock(ticker_name="MSFT", period=period),
                     offer_price=95, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The spread mainly exists due to regulatory
                                    concerns over MSFT's potential abuse of power and potential restriciton of ATVI
                                    games solely to Xbox console. UK and European antitrust watchdogs, among others
                                    have started their inquiries into the transaction. EU Commission has extended it's
                                    deadline for a decision til Apr'23. This month, Chinese regulators rejected the
                                    simplified filling request for the merger. Recent rumors on the merger suggest that
                                    FTC plans to block the merger. Warren Buffet's Berkshire is also participating in
                                    this merger arb play providing some confidence in the successful outcome and/or
                                    a well-protected downside on ATVI standalone basis."""),
           Arbitrage(target=Stock(ticker_name="IRBT", period=period), buyer=Stock(ticker_name="AMZN", period=period),
                     offer_price=61, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 8, 31, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The spread has widened from 5% to over 15% as market
                                started pricing in higher likelihood of regulatory hurdles. Two months ago the parties
                                received the 2nd request from the FTC. Soon after, several senators began pushing the FTC to
                                block the transaction. Concerns were raised regarding potential privacy infringements and
                                Amazon's history of anti-competitive acquisitions. FTC review is ongoing."""),
           Arbitrage(target=Stock(ticker_name="SAVE", period=period), buyer=Stock(ticker_name="JBLU", period=period),
                     offer_price=31, additional_buyer_ratio=0,
                     expecting_closing=datetime(2024, 6, 30, tzinfo=timezone.utc),
                     commentary=r"""**Main risk** - regulatory approval. The current soread is mainly due to antitrust
                                    concerns. DOJ has issued a second request and is currently reviewing the merger.
                                    JBLU has proposed divestitures in overlapping areas - this could alleviate
                                    antitrust concerns. Moreover, SAVE recently reached agreement with pilots union.
                                    Another DOJ concern relates to JBLU's Northeast Alliance partnership (NEA) with
                                    American Airlines. In October, a motion to dismiss the DOJ case against NEA has been
                                    denied. Now the decision comes down to the judges reading of andtrust law which
                                    could signincantly delay the decision. Hence, SAVE_JBLU merge outcome might also
                                    depend on the outcome of NEA trial, last month. JBLU's management reiterated
                                    confidence in merger closing in H1'24"""),
           Arbitrage(target=Stock(ticker_name="BKI", period=period), buyer=Stock(ticker_name="ICE", period=period),
                     offer_price=68, additional_buyer_ratio=0.144,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. Shareholders have already approved the merger. However,
                                Community Home Lender Association has called regulators to block the merger over antitrust
                                concerns saying that the combined company will have too much pricing power in the small/medium
                                mortgage banking sector. The companies each hold dominant market shares in speicfic US mortgage
                                software segments - servicing (BKI) and origination (ICE) - suggesting the merger will lead to
                                substantial vertical integration. Recently ICE agreed to an extended FTC review with reiterating
                                its expectation merger completion by H1'23. Since then, however, a congresswoman came
                                out, urging the FTC to tightly scrutinize the transaction
                                """),
           Arbitrage(target=Stock(ticker_name="TGNA", period=period),
                     buyer="Standard General", offer_price=24.15,
                     additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 2, 28, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The buyer consortium includes Standard General,
                                Apollo, and Cox Media. Various industry players and unions have voiced their concerns
                                that combined TGNA/Cox Media will control too much of the market share (39% of U.S. TVH)
                                Other concerns include potential staff reductions, lower local news coverage and
                                renegotiations of retransmission fees. Analsis of TGNA and Cox Media's US household
                                coverage suggests that the combined company would still be withing the limits of FCC
                                ownership rules, whereas the merger will not affect competition. Recently Telecom
                                regulators noted they have no objections to the merger. However, both FCC and DOJ
                                reviews are still ongoing. Merger end date has now bee extended till Feb'23.
                                """),
           Arbitrage(target=Stock(ticker_name="TSEM", period=period), buyer=Stock(ticker_name="INTC", period=period),
                     offer_price=53, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 12, 31, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The merger will require numerous antitrust
                                and foreign investment approvals. Intel's CEO has noted that regulatory clearance has
                                already been received in several geographies. The transaction continues to be held up
                                by Chinese regulators, which have been increasing scrutinty over the merger in a
                                strategically important semiconductor space. For the same reason there is uncertainty
                                regarding Israel's government approval. Israel withholding taxes will apply in case of
                                succesfull closing - to avoid tese foreign investors will be required to provide some
                                paperwork, which might delay the eventual payout of the merger consideration and might
                                explain part of the spread.
                                """),
           Arbitrage(target=Stock(ticker_name="VMW", period=period), buyer=Stock(ticker_name="AVGO", period=period),
                     offer_price=71.25,
                     additional_buyer_ratio=0.125,
                     expecting_closing=datetime(2023, 10, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - long timeline/regulatory review. This is mammoth \\$61bn deal,
                                giving Broadcom a push into the software industry. A long and detailed probe from EU
                                regulators is expected. Broadcom's CEO has noted that regulatory filings have so far
                                seen good progress in numerous grographies. The merger could take more than a year to
                                complete.
                                """),
           Arbitrage(target=Stock(ticker_name="ACI", period=period), buyer=Stock(ticker_name="KR", period=period),
                     offer_price=27.25, additional_buyer_ratio=0,
                     expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. US senators have raised anticompetitive concerns
                                to the FTC. To satisfy potential regulatory hurdles ACI and KR proposed divesting a
                                large number of stores. Also, as part of the merger agreement, ACI had to pay a
                                \\$6.85\\/share special dividend to its shareholders. However, several states filed a
                                lawsuit to block the payment arguing it would weaken the company's ability to compete
                                as the antitrust reviews proceed. Court's hearing has now been delayed till the 9th Dec.
                                Management remains confident that divestments will be enough to satisfy potential
                                regulatory concerns while also stating that a lawsuit related to divident payments is
                                groundless and should ger resolved in court.
                                """),

           Arbitrage(target=Stock(ticker_name="SIMO", period=period), buyer=Stock(ticker_name="MXL", period=period),
                     offer_price=93.54,
                     additional_buyer_ratio=0.388,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - Chinese regulatory approval. Approval from China's regulators is the main hurdle.
                                The buyer is based in the U.S, while the target is a US-listed Taiwanese company with China being
                                its largest market. Both parties had previously filed under the simplified procedures, but have
                                now re-filed under a normal procedure as advised by Chinese regulators. This month the documents
                                have been accepted and regulatory review is underway.
                                Management reiterated the expected closing date to be in mid-late 2023."""),
           Arbitrage(target=Stock(ticker_name="IAA", period=period), buyer=Stock(ticker_name="RBA", period=period),
                     offer_price=10, additional_buyer_ratio=0.5804,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - shareholder approval. The current spread largely reflects the risk of IAA
                                shareholder approval (meeting date TBD). Recently, reputable activist Ancore (4% stake)
                                voiced its opposition to the merger, arguing that it undervalues the company. Given the
                                strong strategic rationale and relatively low transaction multiple, there is a decent
                                chance for an improved offer. Both parties seem confident that regulatory approvals will pass.
                                """),
           Arbitrage(target=Stock(ticker_name="HVBC", period=period), buyer=Stock(ticker_name="CZFS", period=period),
                     offer_price=6.1, additional_buyer_ratio=0.32,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - expensive hedging. The key reason for the spread is high borrow fees,
                                currently standing at 13%. Merger is expected to close succesfully by H1'23. Both
                                shareholder and regulatory approval are likely to pass given the larget premium over
                                the historical TBV as wll as the small size of the combined enterprise.
                                """),
           Arbitrage(target=Stock(ticker_name="SJR", period=period), buyer=Stock(ticker_name="RCI", period=period),
                     offer_price=30.12, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. Regulators have blocked the transaction saying
                                it will significantly dampen competition in Canda (where telecom rates are already
                                among the highest in the world). To alleviate antitrust concerns, the companies have
                                in turn agreed to divest RCI's wireless service division. However, Canada's Competition
                                Committee recently stated that the proposed divestment is not an effective remdey.
                                Anticipated settlement during the attempted mediation has failed. This month, the
                                heaing started a competition Tribunal. Both parties expect to receive regulatory
                                clearance sometime in 2023.
                                """),
           Arbitrage(target=Stock(ticker_name="FCRD", period=period), buyer=Stock(ticker_name="CCAP", period=period),
                     offer_price=1.89,
                     additional_buyer_ratio=0.2063,
                     expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - NAV volatiltiy. This is essentally a NAV for NAV merger with an
                                additional cash portion from buyer's external manager. Final consideration will be
                                determined at the time of closing, which is expected in Q1'23. The spread likely exists
                                due to small capitalization, somewhat confusing consideration calculations, and unknown,
                                but predictable transaction expenses. The main risk is NAV volatility, however, due to
                                short timeline NAV changes are likelty to be minimal.
                                """),
           Arbitrage(target=Stock(ticker_name="FORG", period=period), buyer="Thoma Bravo", offer_price=23.25,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - antitrust approval. FORG is getting acquired by PE firm Thoma Bravo.
                                The main risk is regulatory approval due to increased market concentration. Just this
                                year Thomas Bravo has already acquired 2 players in the IAM space - one of which is a
                                direct peer to FORG. Recently, reports came out that Thomas Bravo plans to pull and
                                refile its merger docs with DOJ. Merger is expected to close in the first half of 2023.
                                """),
           Arbitrage(target=Stock(ticker_name="SGFY", period=period), buyer=Stock(ticker_name="CVS", period=period),
                     offer_price=30.5, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The reason for the small spread is still pending
                                regualtory approval. Recently FTC requested additional information due to
                                anti-competitive concerns of the proporsed merger. CSV's managements suggests the deal
                                will pass as both companies provide different products and services. Merger is expected
                                to close in H1'23.
                                """),
           Arbitrage(target=Stock(ticker_name="GSMG", period=period), buyer="Management", offer_price=1.55,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - Chinese company and material downside. The price was already raised
                                once from the initial \\$1.27\\/share, which was rejected by the special committee. An
                                improved offer was appoved and a definitive agreement is now in place. Major shareholder
                                US hedge fund Shah Capital is rolling its 11% stake. Shareholder approval has been granted.
                                Downside is very material, which coupled with GSMG being a Chineese company, probably
                                explains the current spread.
                                """),
           Arbitrage(target=Stock(ticker_name="CCHWF", period=period), buyer=Stock(ticker_name="CRLBF", period=period),
                     offer_price=0,
                     additional_buyer_ratio=0.5579, expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary=r"""**Main risk** - potential dilution to the consideration due to certain earn-out
                                provisions, regulatory approval and the buyer walking away. The merger has received
                                shareholder approval. Some asset divestitures required by the regulators have already
                                been announced. The spread, however, has recently widened given failed attempts to
                                pass the federal marijuana banking legislation which has made a big negative impact
                                on the sector's short-term outlook. This has raised the risk of total proceeds from
                                divestitures not reaching the targeted \$300m. The market seems to think that both
                                sides will be unable to complete the divestitures. Also, the merger exchange ratio
                                is subject to proration adjustment by the amount of Columbia Care shares issued as an
                                earn-out for its historical acquisition from Dec'20. Information on the earn-out is
                                limited but the maximum stated size is \$58m in CCHW shares. At current prices,
                                 the maximum earn-out would lower the exchange rate to 0.5174 and reduce the spread to 23%.
                                """), ]
    return sorted(res, key=lambda x: x.expecting_closing)
