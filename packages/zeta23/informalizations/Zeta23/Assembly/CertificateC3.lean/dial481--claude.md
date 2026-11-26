---
{
  "module": "Zeta23/Assembly/CertificateC3.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/CertificateC3.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/CertificateC3.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Assembly/CertificateC3.lean — the count certificate for the rank–trace inequality with parameter
c = 3 (distinct zeros), following Assembly/Certificate.count_certificate with the c = 3 fixed-T algebra:
from the seam shape 6·tr Ĝ − ‖Ĝ‖² − 3N − 5NII − B(6 + 2√‖Ĝ‖² + B) ≤ 2·lower (the c = 3 seam
carries 5·NII: 3 from −3N(I′) and 2 from 2·#𝒵(I′) ≤ 2N_d + 2NII) and the moment
hypotheses tr Ĝ ≥ (1−δ)N, ‖Ĝ‖² ≤ (κ+δ)N (every δ > 0), eventually (3/2 − κ/2 − ε)·N ≤ lower.
-/
```

### `count_lower_moment_c3_five`

 the c = 3 fixed-T algebra with the 5·NII window term. 

### `count_certificate_c3`

 **the c = 3 count certificate.** 
