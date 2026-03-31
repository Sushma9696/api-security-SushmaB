1) What are the real-world consequences of exposing an API key on GitHub?

Exposing a key on GitHub isn't just a "best practice" issue; it has immediate, high-stakes consequences. Bots constantly crawl public GitHub repositories specifically looking for keys.

Financial Theft (The "Bot" Attack): Attackers use leaked keys to run high-cost services. For example, if an AWS key is leaked, bots can spin up massive crypto-mining servers. Developers have reported bills exceeding $1,000 to $10,000 within hours of an accidental push.

Service Hijacking & DoS: If an attacker steals your OpenWeatherMap key, they can exhaust your 60 calls/minute limit. This causes a Denial of Service (DoS) for your actual patients, who will see errors instead of life-saving weather alerts.

Data Breach Roadmap: A leaked key acts as a "front door" for hackers. Once inside your API ecosystem, they can often discover other vulnerabilities, such as your backend endpoints or database structures, leading to a broader system compromise.

2) Why does your company's privacy policy prohibit logging city names?

In healthcare, even a simple city name is considered a "sensitive identifier." Our company policy aligns with major privacy frameworks like HIPAA (USA) and GDPR (EU).

The "De-identification" Principle
Under HIPAA, location data (like city names or zip codes) is one of the 18 identifiers that must be protected. When you log Fetching weather for: Hyderabad, you are creating a permanent record of where a patient is seeking care.

Re-identification Risk: While a city name alone seems harmless, an attacker who gains access to your logs could combine that city with a timestamp. If they already know a specific patient was at the clinic at 10:00 AM, the log confirms their identity and medical visit.

Data Minimization (GDPR): This principle states that a company should only collect and store the absolute minimum amount of data needed. Since the app only needs the city to fetch the weather, storing it in a log file serves no functional purpose and only creates a liability.

Legal & Financial Fines: Under GDPR, failing to protect personal data can result in fines up to €20 million or 4% of annual turnover.

