---
{
  "module": "proof/rates/ClauseBound/ParityChecks/CertOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/CertOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates for the count through parity checks

The program of proof/rates/ClauseBound/ParityChecks/ProgDefs.lean is polynomial-time (PolyT) in the
pad, the index of the clique solver, the numbers n and Δ in unary and the formula: the numbers of
marks that a profile
prescribes (`tl`), the weight of a profile (`GW`), the clauses of the incidences (`incL`), one
evaluation (`evW`), the two functions that the choice of the checks asks (`orcA`, `orcB`), the
choice of the
checks (`runToF`, `runF`, folds whose state the pad cuts off after every round) and the count
(`countOL`). The end is `stCertCountOL`, the interface statement `StCertCountOL`.

The certificates of the value of a network through the solver, of the network of marks and of the
test for admissible profiles are hypotheses, as in proof/rates/ClauseBound/TopN/Cert.lean. The
certificate of one
decision (`StDec`, proved below from a lemma of proof/rates/ClauseBound/ParityChecks/CertNum.lean)
asks for the number of the clause in unary. In the loop over the clauses 0, …, e − 1 that number is
replaced by its minimum with e, which
changes nothing. 

### `StDec`

 One decision is polynomial-time, for the number of the clause in unary and any two
polynomial-time functions in the place of the sums over marks. 

 ### The weight of a profile and the clauses of the incidences 

### `tl_unary`

 The number of marks that a profile prescribes for a layer is given in unary, for the number of
nodes in unary. 

### `GW_polyT`

 The weight of a profile is polynomial-time, for the number of layers and the numbers of marks in
unary. 

### `incL_polyT`

 The clauses of the incidences are polynomial-time, for the number of complete checks in unary. 

 ### The program 

### `CU`

 What the program reads from the context: the pad and the index are polynomial-time, n and Δ are
given in unary, and the parameters `q` satisfy `QU`. 

### `CU.comp`

 The property passes to a polynomial-time change of the context. 

### `Given`

 The certificates that come from elsewhere. 

### `evW_polyT`

 One evaluation is polynomial-time. 

### `orcA_polyT`

 The first of the two functions that the choice of the checks asks is polynomial-time. 

### `orcB_polyT`

 The second of the two functions that the choice of the checks asks is polynomial-time. 

### `runToF_polyT`

 The decisions for one check are polynomial-time, for their number in unary. 

### `runF_polyT`

 The choice of all checks is polynomial-time. 

### `countOL_polyT`

 The count is polynomial-time. 

### `stCertCountOL_of`

 The count of one sparse formula through parity checks is polynomial-time, given the certificates
of the value of a network through the solver, of the network of marks, of the test for
admissible profiles and of one decision. 

### `stDec`

 The certificate of one decision, in the form in which it is used here. 

### `stCertCountOL`

 The count of one sparse formula through parity checks is polynomial-time, given the certificates
of the value of a network through the solver, of the network of marks and of the test for
admissible profiles. 
