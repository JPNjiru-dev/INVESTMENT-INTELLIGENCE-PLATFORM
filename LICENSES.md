# License Inventory

**State:** Initial bootstrap; no product license selected.

| Component/source | Version/ref | License | Intended use | Review |
|---|---|---|---|---|
| PROJECT_CODENAME source | Initial repository bootstrap and instrument-domain increment | No license declared | Proprietary product repository by default; confirm policy before publishing code | No third-party code included |
| revenue-assurance-engine sibling | main at audit time | MIT declared by repository metadata and LICENSE | Reference only; no code copied | Any future reuse requires file-level review and attribution |
| Python runtime | 3.12 (local validation environment) | PSF-2.0 | Standard-library use only; runtime is not bundled or redistributed | No third-party dependencies introduced |
| actions/checkout | v7.0.1, 3d3c42e5aac5ba805825da76410c181273ba90b1 | MIT | CI source checkout only | Pinned to signed upstream commit; see THIRD_PARTY_NOTICES.md |
| actions/setup-python | v7.0.0, 5fda3b95a4ea91299a34e894583c3862153e4b97 | MIT | CI Python runtime setup only | Pinned to signed upstream commit; see THIRD_PARTY_NOTICES.md |
| Everything else | — | — | None | No dependencies introduced |

For each new direct or transitive dependency, record package, exact version, license/SPDX identifier, source, distribution/notice obligations, and review result. Do not infer a license from public visibility. No product license change without explicit approval.
