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
             Stock("GPRE", period=period, interval=interval,
                   expectation=Expectation(price=60, date=datetime(2024, 4, 2, tzinfo=timezone.utc)),
                   description=r"""Green Plains is transitioning from a legacy ethanol company into a diversified bio-refinery after the
                                   acquisition of Fluid Quip in 2020. The company is now at an inflection point where the market will start
                                   to see a meaningful increase in financial performance. Half of GPRE’s facilities have already been converted
                                   to include these AgTech enhancements while the remainder should be converted within 18 months.
                                   Q1’23 earnings will mark the beginning where half of GPRE’s platform runs at planned production capacity
                                   Activist Ancora is now pushing for strategic alternatives, including a sale, suggesting a strategic acquirer
                                   could pay \$50/share or more. GPRE trades at <5x E2023 EBITDA of around \$450m.
                                   Company is worth around \$60-\$65/share over the next 12-18 months.
                                   [Source](https://twitter.com/InvestSpecial/status/1642450715284062208)"""),
             Stock("RMBL", period=period, interval=interval,
                   expectation=Expectation(price=25, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""RumbleOn is the largest power sports dealership group in the US. Currently, RMBL is misunderstood and
                                   being viewed as yet another COVID beneficiary. However, RMBL is sufficiently resilient during near-term
                                   macro bumpiness and has a compelling LT strategy for value creation. RMBL’s organic growth, with used
                                   volume growth being the key component, will allow the company to outperform peers this year.RMBL has
                                   multiple levels to create value including accretive M&A, opening their fulfillment/distribution centers
                                   to the public, and focusing on effective servicing at dealerships. Despite high leverage, the risk of
                                   breaching debt covenants is low. 2024 EBITDA expected at around \$130m. Using a 6x EBITDA multiple results
                                   in a \$25/share price target.
                                   [Source](https://twitter.com/InvestSpecial/status/1642450715284062208)"""),
             Stock("BAIN.PA", period=period, interval=interval,
                   expectation=Expectation(price=150, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""SBM: A unique investment in the ultra-rich – with operating leverage and growth.
                                   If even part way accurate, this analysis suggests significant potential upside on a post-COVID recovery
                                   as the rentals are revalued. We view a more appropriate valuation as closer to €150/share for the group.
                                   [Source](https://east72.com.au/wp-content/uploads/2023/04/E72DT-QUARTERLY-REPORT-Mar-2023.pdf)"""),
             Stock("APT", period=period, interval=interval,
                   expectation=Expectation(price=4.5, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Relatively mediocre business, however, it is cheap on all metrics. Trades at 7x EBIT, slightly above net
                                   current assets. Well-protected downside and meaningful potential upside.The company manufactures/sells
                                   single-use protective apparel products and building supply products. Net cash balance sheet and rational
                                   capital allocation strategy. Uses all FCF to buy back stock, S/O declined from 27m in 2006 to 13m today.
                                   Shares might skyrocket on the next viral outbreak, as has already happened due to H1N1 in 2009 and COVID in 2020.
                                   Attractive M&A target for both financial and strategic buyers.Shares might skyrocket on the next viral outbreak,
                                   as has already happened due to H1N1 in 2009 and COVID in 2020. Attractive M&A target for both financial and
                                   strategic buyers. EV/sales at 0.52x, EV/EBIT is 6.8x, and EV/NOPAT is 8.6x.
                                   NCAV per share is \$3.77 (1.14x) and TBVPS is \$4.85 (0.89x). Exp. gain: TBVPS is set to compound at 8%
                                   annually in the absence of any viral outbreaks.
                                   [Source](https://twitter.com/InvestSpecial/status/1643537169309483008)"""),
             Stock("AUE.SI", period=period, interval=interval,
                   expectation=Expectation(price=1.15, date=datetime(2023, 6, 30, tzinfo=timezone.utc)),
                   description=r"""An interesting special situation play with a very limited downside. Golden Energy and Resources
                                   is a holding company of two publically listed coal subsidiaries. It is currently subject to a
                                   takeover proposal by the controlling shareholder. Original lowball offer was raised by 17% after
                                   Singaporean minority investor ‘watchdog’ called for an improved bid. The amended offer was not
                                   declared final and there is a decent chance it gets raised again. Buyer looks motivated to get the deal done.
                                   Offer is expected to be raised to around 108-115 cents.
                                   [Source](https://twitter.com/InvestSpecial/status/1642823074541182976)"""),
             Stock("CEG", period=period, interval=interval,
                   expectation=Expectation(price=115, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Constellation Energy, a recent spinoff, operates 13 nuclear power plants in the US. As of the
                                   Inflation Reduction Act’s (IRA) subsidies, CEG thus offers a minimum FCF yield of around 8.5%
                                   while allowing for full upside potential at higher power prices.  Furthermore, the downside looks
                                   somewhat protected as the company trades at <50% below replacement cost. The stock offers additional
                                   optionality if the company takes advantage of IRA-supported tax-credit opportunities in clean hydrogen.
                                   12-13x EBITDA multiple on floor earnings implies a \$115-125/share stock price.
                                   [Source](https://twitter.com/InvestSpecial/status/1642823074541182976)
                                """),
             Stock("PENN", period=period, interval=interval,
                   expectation=Expectation(price=85, date=datetime(2025, 1, 30, tzinfo=timezone.utc)),
                   description=r"""Casino operator with 43 properties + digital assets. Since pre-pandemic, sales grew by 20% and
                                   margins significantly improved. Despite these positives, PENN trades at the same EV as pre-covid.
                                   Core business comprises 85% of revenue and provides solid downside protection.
                                   On top of that, PENN's digital assets present a call option on OSB/iCasino industry. Both digital
                                   assets continue to grow and are at breakeven now. Sustainable margin improvement has been mainly
                                   achieved through cost savings. Management's compensation is heavily tied to share price appreciation
                                   over the next 3 years. The company has started buying back shares. Land-based businesses are expected
                                   to deliver ~\$5/share of levered FCF by '25. At today's 11x multiple, that's \$55/share value.
                                   Digital assets are worth an additional \$30/share.
                                   [Source](https://twitter.com/InvestSpecial/status/1644625210794995713)"""),
             Stock("LNW", period=period, interval=interval,
                   expectation=Expectation(price=150, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Gaming content creator/manufacturer/distributor for land-based and digital casinos. Oligopoly with
                                   75% recurring revenue and high switching costs. Has now assembled an all-star team after hiring
                                   around 50 high-level executives from rival Aristrocrat. Core business is expected to benefit from
                                   an increase in casino CAPEX following two years of negligible spending. Also, market is currently
                                   ascribing nearly 0 value to LNW’s two digital assets – digital casino games and mobile/social gaming.
                                   Digital assets are highly synergistic to its main business and are expected to benefit from digital
                                   casino legalisation in the US and growing TAM for mobile/social gaming.
                                   LNW trades 6.5x 2024 EBITDA vs 10x for closest peer Aristocrat. Optionality to re-rate closer to
                                   video game focused peers (trade at 17-19x EBITDA). Stock is expected to return 3.7x MOIC.
                                   [Source](https://twitter.com/InvestSpecial/status/1644625210794995713)
                   """),
             Stock("SOMA.V", period=period, interval=interval,
                   expectation=Expectation(price=6, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Imagine you can invest in gold as a safe haven, but with the characteristics of an exponential tech stock.
                                   If Soma Gold proves they have the resources, it could simply expand annual production from 36K to 75K.
                                   This growth is already permitted and should give us a 10 bagger. I believe Soma Gold is going to be
                                   Segovia 2.0 as they are also starting at 500K ounces of resource and 50K ounces of production.
                                   Over time this will grow to multimillion ounces of resource and 100K+ ounces of production.
                                   Catalysts: Drill results update coming. 3 drill rigs on site + 1 drill rig incoming this month.
                                   AISC will be below \$1000/ounce due to mechanized mining. Gold loan is fully repaid in January.
                                   Long term note repayment starts in July. Production will increase from 35K to 50K
                                   [Source](https://twitter.com/GoldForecast/status/1646418350996705283)
                  """),
             Stock("TM.V", period=period, interval=interval,
                   expectation=Expectation(price=1.5, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Trigon Metals Inc. (TM:TSXV) is a Canadian exploration, development, and mining company focused on copper
                                   and silver assets in Africa. Trigon’s current priority is the restart of its flagship project, the Kombat
                                   Mine in Namibia. The Kombat Mine was once one of the largest copper producers in Namibia having historically
                                   produced 12.5 Mt of ore at 2.6% Cu. Trigon plans to bring Kombat back into production in FY23 with 4.0 Mlbs
                                   of copper expected to be mined in FY24 and growing to 22.1 Mlbs by FY26.
                                   [Source](https://mcusercontent.com/4bc421505c66d079778a0d0be/files/95cf91a8-23ab-97c9-b8ba-0f921b470b3e/20230403_Atrium_TM_Initiation_Report.02.pdf)
                   """),
             Stock("EHTH", period=period, interval=interval,
                   expectation=Expectation(price=25.38, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""eHealth is a digital health insurance broker with secular tailwinds from the continued Medicare Advantage
                                   growth till 2040. EHTH was classified as an un-investable stock in an un-investable industry on top of a
                                   damning short report from Muddy Waters. Report pointed to low-quality earnings due to mandatory ASC606
                                   adoption and abusing its constraints with aggressive growth tactics. EHTH is in a turnaround mode with new
                                   mgmt, reversing bad growth policies and industry players behaving more disciplined. Churn is expected to
                                   stabilize back to normalized levels. 100% upside opportunity protected by a floor valuation.
                                   The liquidation value of the commissions receivables is higher than the current market cap.
                                   Depending on the assumed churn levels, the stock has 70% upside in the base case and 400% upside for the
                                   bull case. BV of commissions receivables is \$25.38/share after net debt and preferred
                                   [Source](https://twitter.com/InvestSpecial/status/1649352951897415680)
                   """),
             Stock("BGEO.L", period=period, interval=interval,
                   expectation=Expectation(price=80, date=datetime(2025, 12, 31, tzinfo=timezone.utc)),
                   description=r"""BGEO is a London-listed leading retail and commercial bank in the country of Georgia.
                                   The bank operates in an attractive duopoly market with strong and improving country-level fundamentals.
                                   Should benefit from the recent influx of Russian immigrants. BGEO trades at just 1x book value and 4x
                                   earnings whilst continuing to return capital through buybacks and dividends. Its Western-trained management
                                   is excellent and has been able to return consistent 20%+ ROEs over the last 15 years.
                                   At a ~6x P/E or ~1.5x P/B 2025 exit multiple, combined with \£6/shr of cum. dividends, stock is
                                   expected to trade at \£80 /shr.
                                   [Source](https://twitter.com/InvestSpecial/status/1649352951897415680)
                   """),
             Stock("OSW", period=period, interval=interval,
                   expectation=Expectation(price=22, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Provider of spa services on cruise ships. Quasi-monopoly with over 90% of the cruise ship market.
                                   Long-term 7-10% topline growth. Trades at 10-12x 2024 FCF. Capital returns coming.
                                   100% upside. Onshore spa competitors face difficulty replicating OSW’s global breadth and scale.
                                   Due to relatively minimal expense, cruise ship operators have no incentives to switch or in-house services.
                                   Historically, churn has been almost nonexistent. Expected to initiate a dividend this year or next at the latest.
                                   Due to minimal capex needs, set to become a cash-flow return machine.
                                   [Source](https://twitter.com/InvestSpecial/status/1650422425018937345)
                   """),
             Stock("RGS", period=period, interval=interval,
                   expectation=Expectation(price=7, date=datetime(2025, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Hair salon franchisor with 5,000 units. Covid-driven headwinds masked the fact that RGS has
                                   wrapped up a major business model transition to the franchised model The business has bottomed
                                   out and is on the path to recovery. Worth \$7, representing a 6x return A recession-proof,
                                   asset-light business that is generating 30%+ EBITDA. The new CEO joined in 2022 and is successfully
                                   turning the business around. Both the business model transition and liquidity profile improvement
                                   have gone unnoticed by the street.
                                   [Source](https://twitter.com/InvestSpecial/status/1650422425018937345)
                   """),
             Stock("CBD", period=period, interval=interval,
                   expectation=Expectation(price=6, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""CBD is a Brazilian holding company that is spinning off its Colombian grocery chain, Grupo Exito,
                                   in the second quarter of 2023. Shareholders will receive 4 shares of Grupo Exito, which is currently
                                   trading at a higher value than CBD's remaining assets (referred to as the "stub"). However,
                                   the stub includes multiple assets that should be worth at least \$0.50/share, as well as a
                                   high-end grocery chain in Brazil. Assuming the stub trades at 0 and Exito is valued correctly,
                                   the potential upside is around 20%. The author believes that both the stub and Exito should be worth at
                                   least \$6.00/share in the long term, which is at least a double from the current price.
                                   [Source](https://www.clarksquarecapital.com/p/companhia-brasileira-de-distribuicao?publication_id=802343&utm_source=substack&utm_medium=email)
                  """),
             Stock("GOGO", period=period, interval=interval,
                   expectation=Expectation(price=28, date=datetime(2027, 12, 31, tzinfo=timezone.utc)),
                   description=r"""In conclusion, Gogo is a high-quality business operating in a structurally growing industry.
                                   The business is well- managed by highly incentivized insiders. The stock is not widely followed by investors
                                   and the investors that are aware of the company do not fully appreciate the business transformation and
                                   turnaround that has taken place. The market is also concerned about growing competitive risks; however,
                                   these fears are likely over-blown and provide an opportunity to buy shares in Gogo at attractive prices.
                                   [Source](https://mcusercontent.com/08f9a0d6280bf283b8bc58473/files/16fa3f9e-10cd-3666-5625-bad7f6c56620/LVS_Advisory_GOGO_Write_Up_April_2022_.pdf?utm_source=substack&utm_medium=email)
                  """),
             Stock("SCHW", period=period, interval=interval,
                   expectation=Expectation(price=80, date=datetime(2023, 9, 15, tzinfo=timezone.utc)),
                   description=r"""SCHW unfairly sold off following the SVB fallout. Market's concerns are misplaced.
                                   SCHW is unlikely to be required to raise cheap equity for regulatory reasons. 81% of deposits
                                   are FDIC insured while the remaining 19% are easily covered by SCHW’s liquid securities portfolio.
                                   Depositors are unlikely to flee. SCHW does not have a negative TBV after adjusting for taxation
                                   on unrealized HTM losses and YTD gains. Set to earn \$4.5bn in an extreme scenario of a pure brokerage
                                   (all deposits flee). Or \$8bn a year in another extreme of deposit sorting stopping today.
                                   This compares to $\94bn market cap.
                                   [Source](https://twitter.com/InvestSpecial/status/1651887289553780737)
                   """),
             Stock("DEA", period=period, interval=interval,
                   expectation=Expectation(price=17, date=datetime(2023, 8, 15, tzinfo=timezone.utc)),
                   description=r"""Cheap low-risk REIT that leases class A office properties to US govt agencies. The highest quality tenant in the world.
                                   Low renewal risk and vacancy of only 1.2%. 8% dividend is sustainable. Much higher
                                   return than treasuries, but with similar risk.Strong balance sheet with low-cost fixed-rate
                                   debt with no significant near-term maturities. Debt/EV at 46%. Solid management with
                                   longstanding relationships with various government agencies.Trades at 11.5x 2022 FFO and
                                   12x E2023 FFO whilst offering an 8% dividend yield.
                                   [Source](https://twitter.com/InvestSpecial/status/1651887289553780737)
                   """),
             Stock("GB", period=period, interval=interval,
                   expectation=Expectation(price=20, date=datetime(2023, 10, 15, tzinfo=timezone.utc)),
                   description=r"""A less visible and safer bet on China reopening. Provider of VAT tax refund services for international
                                   travelers, ~70% market share. Essentially a small royalty on travelers purchasing luxury goods abroad.
                                   As China re-opens profits will inflect above pre-COVID. Some re-opened regions are spending 3x on like
                                   for like basis through GB vs what they were pre-COVID. This business has 80% incremental margins from
                                   any new revenue, >40% EBITDA margins, and 85% FCF conversion. Trades <10x 2019 EBITDA, without any credit
                                   for dramatically higher luxury goods prices or cost take-outs since then.
                                   As China reopens, GB could do \$1+/share of FCFresulting in a \$20+ stock.
                                   [Source](https://twitter.com/InvestSpecial/status/1653327568173400067)
                   """),
             Stock("IWG.L", period=period, interval=interval,
                   expectation=Expectation(price=430, date=datetime(2030, 1, 1, tzinfo=timezone.utc)),
                   description=r"""Global operator of flexible working spaces with 4x the locations of their next-largest competitor.
                                   Currently in the early stages of transferring the majority of the current business into the
                                   franchised operations. If successful, would result in the transfer of a significant part of lease
                                   liabilities and the cost base onto a 3rd parties. This would leave IWG with a far higher margin royalty
                                   stream likely to be valued by the market on a more generous multiple. The currently large operating lease
                                   liability (even if non-recourse and tied to individual properties) is a significant concern among investors.
                                   Set to generate 29p EPS by 2025, 55p by 2030. SOTP: mature estate + franchised business + The Instant Group,
                                   results in 430p fair value today."""),
             Stock("MTB", period=period, interval=interval,
                   expectation=Expectation(price=260, date=datetime(2028, 1, 1, tzinfo=timezone.utc)),
                   description=r"""The bank is oversold on fears caused by the collapse of SVB and other banks.
                                   However, MTB is run by a conservative mgmt team in markets with stickier deposit bases.
                                   That does not make them immune to dumb ideas, but it greatly reduces the risk to shareholders.
                                   MTB has consistently earned mid-teens ROTE. Pays out a healthy dividend, and uses excess capital
                                   to buyback stock. Last year's merger with People's United provides significant scale benefits,
                                   which should become evident shortly. In 2022, MTB earned \$14.42 per share.
                                   Expected to earn north of \$20/share in 4-5 years, with excess cash used for buybacks.
                                   At 13x multiple would be a \$260 stock.
                                   [Source](https://twitter.com/InvestSpecial/status/1656583775957008385)
                   """),
             Stock("GEO.TO", period=period, interval=interval,
                   expectation=Expectation(price=7.3, date=datetime(2024, 3, 15, tzinfo=timezone.utc)),
                   description=r"""Drilling company providing sample extraction services for gold miners in Africa and South America.
                                   Trades at 2.4x TTM EV/EBITDA despite highly recurring revenue, and positive FCF while growing both
                                   the revenues and earnings at a decent clip. Low trading multiple should expand as investors realize
                                   we are at the beginning of a long cycle of growth for the industry. Increasing free cash flow allows
                                   GEO to continue returning capital to shareholders through dividends and share buybacks.
                                   An attractive target to other drillers due to its long-term relationships with mining companies.
                                   CEO with 39% ownership of GEO said openly that he is open to sale at 5x EBITDA or more.
                                   In a sale scenario GEO is worth at least 5x E2024 EBITDA, which implies a C\$7.3/share price target."""),
             Stock("PKN.WA", period=period, interval=interval,
                   expectation=Expectation(price=180, date=datetime(2028, 3, 15, tzinfo=timezone.utc)),
                   description=r"""In my opinion ORLEN has the potential the be an investment comparable to PetroChina.
                                   I am bullish on oil prices and ORLEN gives me trough the ridiculously low valuation a good downside protection.
                                   Here is another quote from Buffet regarding PetroChina.
                                   [Source](https://moderninvesting.substack.com/p/the-next-petrochina)"""),
             ]

    def yield_per_day(x):
        y = (x.expectation.price - x.history.iloc[-1]["Open"]) / x.history.iloc[-1]["Open"] * 100.0
        d = (x.expectation.date - x.last_date).days
        return y / d

    return reversed(sorted(ideas, key=yield_per_day))


def stocks(period: str, interval: str):
    res = []
    for ticker_name in ["TGNA", "CEG", "SOMA.V", "TM.V", "FTAI", "CRNT", "ATLX", "FIP", "CBD", "SCHW"]:
        buy_date = None
        description = None
        if ticker_name == "TGNA":
            buy_date = datetime(2022, 12, 1, tzinfo=timezone.utc)
            description = "Arbitrage"
        elif ticker_name == "CEG":
            buy_date = datetime(2022, 12, 6, tzinfo=timezone.utc)
            description = """Constellation Energy Corporation, formerly Constellation Newholdco, Inc., is a clean
                             energy company. The Company is focused on carbon-free electricity. It is a supplier
                             of clean energy and sustainable solutions to homes, businesses, public sector, community
                             aggregations and a range of wholesale customers, such as municipalities, cooperatives.
                             Utility, energy.
                             See CEG in Ideas.
                          """
        elif ticker_name == "SOMA.V":
            buy_date = datetime(2023, 4, 17, tzinfo=timezone.utc)
            description = r"""Imagine you can invest in gold as a safe haven, but with the characteristics of an exponential tech stock.
                              If Soma Gold proves they have the resources, it could simply expand annual production from 36K to 75K.
                             """
        elif ticker_name == "TM.V":
            buy_date = datetime(2023, 4, 17, tzinfo=timezone.utc)
            description = r"""Trigon Metals Inc. (TM) is a Canadian exploration, development, and mining company focused on copper
                                and silver assets in Africa."""
        elif ticker_name == "FTAI":
            buy_date = datetime(2023, 4, 17, tzinfo=timezone.utc)
            description = r"""Aircraft and engine lessor that has gone through a major transformation from a complex “mess” of
                              assets to a pure-play aviation company."""
        elif ticker_name == "CRNT":
            buy_date = datetime(2023, 4, 20, tzinfo=timezone.utc)
            description = r"""Vendor for global wireless network operators specializing in backhaul solutions. Shareholders have
                                recently rejected a hostile takeover by peer $AVNW at $3.8/share. Renewed talks between AVNW and CRNT
                                present the potential for near-term upside realization."""
        elif ticker_name == "ATLX":
            buy_date = datetime(2023, 4, 24, tzinfo=timezone.utc)
            description = r"""Meme stock, lithium :P"""
        elif ticker_name == "FIP":
            buy_date = datetime(2023, 5, 1, tzinfo=timezone.utc)
            description = r"""Recent spin-off from \$FTAI with 4 infrastructure assets: 3 energy terminals and a railroad business.
                                EBITDA is set to increase from \$140m today to \$250m in the next 12-18 months. FPI’s Jefferson terminal
                                is now on cusp of generating strong earnings. Transtar railroad earnings have been consistently increasing
                                through new business initiatives. Construction of the 485MW power plant at Long Ridge is complete.
                                Downside is well protected at current share price levels."""
        elif ticker_name == "CBD":
            buy_date = datetime(2023, 5, 4, tzinfo=timezone.utc)
            description = r"""CBD is a Brazilian holding company that is spinning off its Colombian grocery chain, Grupo Exito,
                              in the second quarter of 2023. """
        elif ticker_name == "SCHW":
            buy_date = datetime(2023, 5, 16, tzinfo=timezone.utc),
            description = r"""SCHW unfairly sold off following the SVB fallout."""

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
                     offer_price=68, additional_buyer_ratio=0.0682,
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
                     expecting_closing=datetime(2023, 5, 28, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The buyer consortium includes Standard General,
                                Apollo, and Cox Media. Various industry players and unions have voiced their concerns
                                that combined TGNA/Cox Media will control too much of the market share (39% of U.S. TVH)
                                Other concerns include potential staff reductions, lower local news coverage and
                                renegotiations of retransmission fees. Analsis of TGNA and Cox Media's US household
                                coverage suggests that the combined company would still be withing the limits of FCC
                                ownership rules, whereas the merger will not affect competition. Recently Telecom
                                regulators noted they have no objections to the merger. However, both FCC and DOJ
                                reviews are still ongoing. Merger end date has now bee extended till Feb'23.
                                The spread has widened from teen levels to over 40%. Merger end date is set for
                                May 23 after which either party can walk away from the transaction without penalty.
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
           Arbitrage(target=Stock(ticker_name="FORG", period=period), buyer="Thoma Bravo", offer_price=23.25,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - antitrust approval. FORG is getting acquired by PE firm Thoma Bravo.
                                The main risk is regulatory approval due to increased market concentration. Just this
                                year Thomas Bravo has already acquired 2 players in the IAM space - one of which is a
                                direct peer to FORG. Recently, reports came out that Thomas Bravo plans to pull and
                                refile its merger docs with DOJ. Merger is expected to close in the first half of 2023.
                                """),
           Arbitrage(target=Stock(ticker_name="GSMG", period=period), buyer="Management", offer_price=1.55,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary=r"""**Main risk** - Privatization offer withdrawal.
                                    The spread hovered at less than 5% since shareholder approval in Sep'22 as
                                    the market expected prompt merger closing. More than half a year later, the
                                    merger is still pending, meanwhile, the management did not provide any
                                    explanation for 118% why it is taking so long. This scared investors and
                                    the spread gradually widened to above 100%. With the recent annual results release,
                                    the company did not provide any updates on the transaction, noting that the
                                    privatization is "yet to be consummated". The market clearly does not believe the
                                    merger will close as the stock currently trades below pre-announcement levels.
                                    Historically US-listed Chinese privatizations in definitive agreement stage have
                                    had a very high succesful closing rate, However such a prolonged lag indicates elevated
                                    merger break risk.
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
                                """),
           Arbitrage(target=Stock(ticker_name="INFI", period=period), buyer=Stock("MEIP", period=period),
                     offer_price=0, additional_buyer_ratio=1.0449,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary=r"""**Tiny all-stock biopharma merger.**
                                    Main risk - buyer's shareholder approval.
                                    Merger spread stood at minimal levels upon anouncement in Feb'23 and then gradually widened to 50% in March.
                                    This seems to have been driven by the risk of MEIP's shareholder opposition as the transaction terms appear
                                    to be quite 60% unfavorable for the buyer. This is also indicated by MEIP's share price fall of 20% upon
                                    the announcement. As part of the transaction, the buyer is required to keep \$80m in net cash vs \$4m for
                                    INFI while giving away a 42% ownership of the combined entity to INFl's equity holders.
                                    MEIP would add INFI's phase 2 drug candidate to its early-stage pipeline. In liquidation scenario MEIP
                                    could be worth materially above the current share price levels."""),
           Arbitrage(target=Stock(ticker_name="FHN", period=period), buyer=Stock("TD", period=period),
                     offer_price=25, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary=r"""**Largest Canadian bank acquiring a regional US peer.**
                                    **Main risk** - downward price adjustment. The spread on this regional bank merger used to stand at minimal
                                    levels despite still pending regulatory approvals. The spread widen to 20% in March on the news that the
                                    parties will not be able to receive regulatory approvals by the merger 40% outside date of May'23.
                                    The spread increased further to over 40% amid the subsequent banking industry fall-out.
                                    Aside from the pending regulatory aprrovals, the current spread also reflects the risk of a downward price
                                    adjustment given that US bank indices are down significantly since the merger agreement was signed more
                                    than a year ago. The buyer's management has mentioned that negotiations regarding a merger consideration
                                    adjustment are ongoing. TD has remained committed to closing the transaction and the parties are in
                                    discussions to extend the outside date US-listed Chinese company privatization"""),
           Arbitrage(target=Stock(ticker_name="ACI", period=period), buyer=Stock(ticker_name="KR", period=period),
                     offer_price=27.25, additional_buyer_ratio=0,
                     expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
                     commentary=r"""**Merger of two grocery store chains.**
                                    **Main risk** - regulatory approval. Merger of two grocery store chains coming after AC announced strategic
                                    alternatives in 2022. The transaction is synergistic from a geographical perspective - management states
                                    that AC operates in several parts of the country with very few or no Kroger stores. The main risk is
                                    antitrust approvals as the merger would combine the two of the biggest supermarket companies in the country.
                                    US senators as well as a couple of farmer/consumer groups have raised anticompetitive concerns to the FTC.
                                    The buyer KR has already received a second request from the FTC. However, both sides are confident of
                                    circumventing the regulatory hurdles with proposed divestitures of a large number of stores. The companies
                                    have recently started to look for potential buyers of stores in overlapping areas."""),
           Arbitrage(target=Stock(ticker_name="SGEN", period=period), buyer=Stock(ticker_name="PFE", period=period),
                     offer_price=229, additional_buyer_ratio=0,
                     expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
                     commentary=r"""**Prizer's large acquisition in the cancer treatment space.**
                                    **Main risk** - regulatory approval. The current spread seems to exist due to the likely scrutiny from
                                    antitrust regulators and potentially prolonged closing timeline. The transaction would give Pfizer a
                                    leading position in cancer treatment space where the company already owns a sizable portfolio of drugs.
                                    This might increase the combined company's power to negotiate with insurers. Industry analysts have
                                    noted that divestitures in some areas, such as bladder cancer treatment, might be needed. SGEN's shareholder
                                    approval seems likely, given a massive premium to pre-announcement levels. The merger is expected to close
                                    in late 2023-early 2024"""),
           Arbitrage(target=Stock(ticker_name="TCRR", period=period), buyer=Stock(ticker_name="ADAP", period=period),
                     offer_price=0, additional_buyer_ratio=1.5117,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary=r"""**All-stock merger between two clinical-stage biopharmas**
                                    **Main risk** - small capitalization, steep downside, shareholder approvals
                                    The spread exists due to shareholder approval risks. ADAP's share price dropped 25% upon the announcement,
                                    indicating potential equity holder opposition to the deal. Any pushback, however, seems unlikely given that
                                    the transaction is primarily an equity raise for the buyer which is acquiring \$149m of the target's gross cash
                                    for \$64m worth of its stock. The merger would provide ADAP with additional liquidity required to pursue
                                    commercialization of its drug portfolio. TCRR is a cash-burning machine with no commercial-stage assets,
                                    suggesting its shareholders would face dilutive equity raises and/or a prolonged strategic review if the
                                    current deal breaks. TCRR insiders own a sizable 25% of the company. ADAP management owns 17%.""")
           ]
    return sorted(res, key=lambda x: x.expecting_closing)
