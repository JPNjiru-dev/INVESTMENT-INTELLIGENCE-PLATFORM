# License Inventory

**State:** Initial bootstrap; no product license selected.

| Component/source | Version/ref | License | Intended use | Review |
|---|---|---|---|---|
| PROJECT_CODENAME source | Initial repository bootstrap and instrument-domain increment | No license declared | Proprietary product repository by default; confirm policy before publishing code | No third-party code included |
| revenue-assurance-engine sibling | main at audit time | MIT declared by repository metadata and LICENSE | Reference only; no code copied | Any future reuse requires file-level review and attribution |
| Python runtime | 3.12 (local validation environment) | PSF-2.0 | Standard-library use only; runtime is not bundled or redistributed | No third-party dependencies introduced |
| Everything else | — | — | None | No dependencies introduced |

For each new direct or transitive dependency, record package, exact version, license/SPDX identifier, source, distribution/notice obligations, and review result. Do not infer a license from public visibility. No product license change without explicit approval.
