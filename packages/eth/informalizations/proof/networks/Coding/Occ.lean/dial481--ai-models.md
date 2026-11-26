---
{
  "module": "proof/networks/Coding/Occ.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Occ.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Occ.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lean's network of Φ is the printed one with padding

Section 6: «A setting z_a of node a is a bit string with one bit z_a[o] for each occurrence o in
cluster a, and S_a is the set of all these bit strings.» `stOccNet` proves the seven fields of
`Coding.PaddingOf (occNet g Φ) (satNet g 3 Φ) (padOcc g Φ)`:
* the padded string has the bit z_a[o] at the place of o in its cluster (`getD_padOcc_occ`), so
  padding is one to one;
* a string of 3·m̄ bits with 0 at the places without a literal is a padded setting
  (`exists_padOcc`), and elsewhere Lean's W_a is 0;
* Lean's W_a at a padded setting is the printed W_a: «every clause of cluster a has a true
  occurrence» (`clause_iff`) and «z_a[o] = z_a[o'] for every test {o,o'} with both occurrences in
  cluster a» (`inside_iff`);
* z_a|_b is the same string in both networks (`restr_padOcc`), so Ψ_{a,b} = [z_a|_b = z_b|_a] and
  f_{a,b} = [z_a|_b = θ] agree; that Lean's Ψ and f have this form is `Eight.ViaGrouping.satPsi_eq`
  and `satF_eq` (proof/networks/Eight/ViaGrouping/SatPsi.lean).
  `import all StepMachines.Prog.CountNet` gives access to `locals_eq`, `rows_eq` and `boole_congr`,
  which are not public. 

 ### The padded string 

### `length_padOcc`

 A padded setting has 3·m̄ bits. 

### `getD_padOcc`

 The bit of the padded string at place i of the cluster. 

### `place_sub`

 The place of an occurrence of cluster a within the cluster. 

### `getD_padOcc_occ`

 The padded string has the bit z_a[o] at the place of the occurrence o. 

### `getD_map_idxOf`

 A list of values, read at the position of a member. 

### `litAt_local`

 What stands at place r of cluster a. 

### `zero_padOcc`

 A padded setting has 0 at the places without a literal. 

### `exists_padOcc`

 A string of 3·m̄ bits with 0 at the places without a literal is a padded setting. 

### `padOcc_inj`

 Padding is one to one. 

 ### W 

### `clause_iff`

 «every clause of cluster a has a true occurrence», for one clause: Lean's condition at a padded
setting is the printed one. 

### `clauses_iff`

 «every clause of cluster a has a true occurrence»: Lean's condition at a padded setting is the
printed one. 

### `inside_iff`

 «z_a[o] = z_a[o'] for every test {o,o'} with both occurrences in cluster a»: Lean's condition at
a padded setting is the printed one. 

 ### z_a|_b 

### `restr_padOcc`

 z_a|_b is the same string in both networks: «let z_a|_b ∈ {0,1}^{c_{a,b}} list the bits of z_a
at their occurrences in cluster a» (Section 6). 

 ### The seven fields 

### `stOccNet`

 **Lean's network of Φ is the printed one with padding**: «A setting z_a of node a is a bit
string with one bit z_a[o] for each occurrence o in cluster a, and S_a is the set of all these bit
strings» (Section 6), where Lean's settings have one bit for each of the 3·m̄ places of a cluster. 
