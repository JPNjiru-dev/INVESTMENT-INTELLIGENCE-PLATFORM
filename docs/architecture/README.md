# Architecture Map

The repository currently contains product-control documentation only. No application runtime, database, identity, data provider, deployment target, or real-time transport has been selected.

See [Master Blueprint](../MASTER_BLUEPRINT.md) for logical boundaries. Decisions require written evidence and should preserve a modular-monolith starting point until scale requires otherwise.

Initial domain contracts:

- [Instrument identity and conventions](INSTRUMENT_MODEL.md)
- [Point-in-time market bars](MARKET_DATA_CONTRACT.md)
