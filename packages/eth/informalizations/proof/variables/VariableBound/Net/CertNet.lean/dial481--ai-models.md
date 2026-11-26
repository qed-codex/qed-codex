---
{
  "module": "proof/variables/VariableBound/Net/CertNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/CertNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/CertNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «The parameters»: condition (iii) for the network with two kinds of marks

«Counting marks, multiplying powers of 2 and finding the position of a string among those with as
many ones take τ = n^O(1) operations, as condition (iii) requires.» Proved here: one polynomial-time
certificate (`PolyT`, or `Unary` for a number given in unary) for each function of
proof/variables/VariableBound/Net/Defs.lean out of which the network of one profile is made, for
arguments that depend on a context x, with the
number g of nodes in unary and the formula, the list of checks and the profile as data. An argument
of which a docstring says nothing is assumed to be polynomial-time in x. The ends are `stCertNet`
(the lengths of the network `netD` are given in unary and its two functions are
polynomial-time, given `StCertRank` (⌈log C(t, μ)⌉ in unary, positions of strings in polynomial
time)) and `stCertAdm` (the test for admissible profiles is polynomial-time).

The file is the counterpart of proof/rates/PaddedDescent/F/CertMark.lean. The test `okD` is cut into
its four conjuncts, and the weight `WD` into this test, the product of the σ and the exponent of the
sign; each is certified by itself. 

 ### Objects, touches, owners, tests, marks 

### `objs_polyT`

 The list of the objects is polynomial-time in the formula and the list of checks. 

### `obAt_polyT`

 The object at a position is polynomial-time. 

### `clOf_polyT`

 The clause of an object is polynomial-time. 

### `home_polyT`

 The home of a check is polynomial-time. 

### `tchB_polyT`

 The test «the object o touches the node a» is polynomial-time. 

### `tch_polyT`

 The list of the objects that touch a node is polynomial-time. 

### `linkB_polyT`

 The test «{a, b} is a test of the object o» is polynomial-time; g is in unary because the test
runs through all nodes. 

### `ownB_polyT`

 The test «a is the owner of the object o» is polynomial-time, for g in unary. 

### `tst_polyT`

 The list of the objects of a kind with a given test is polynomial-time, for g in unary. 

### `mark_polyT`

 The mark that a setting gives to an object is polynomial-time. 

### `str_polyT`

 The string of the marks of the objects of a kind with a given test is polynomial-time, for g in
unary. 

### `mu_polyT`

 A number prescribed by the profile, one digit of y, is polynomial-time. 

 ### Labels 

### `capD_unary`

 The number c_(a,b) of bits of a label is given in unary, for g in unary, given the certificate
that ⌈log C(t, μ)⌉ is given in unary (`StCertRank`). 

### `labD_polyT`

 The label that a setting shows to another node is polynomial-time, for g in unary, given
`StCertRank` (⌈log C(t, μ)⌉ in unary, positions of strings in polynomial time). 

 ### The weight of a setting 

### `ite_zero_polyT`

 A choice between two integers by the test «i = 0» is polynomial-time. 

### `sig_polyT`

 σ_i is polynomial-time for i given in unary. 

### `qj_unary`

 The number q_j of marked incidences of a check at a node is given in unary. 

### `ok1`

 The first conjunct of `okD`: the value bits of variables with numbers ≥ n are 0. 

### `ok2l`

 One literal in the second conjunct of `okD`: it is not at a, or it is false. 

### `ok2`

 The second conjunct of `okD`: no marked object has a true literal at a. 

### `ok3`

 The third conjunct of `okD`: of each kind, the number of marked objects owned by a is that of
the profile. 

### `ok4`

 The fourth conjunct of `okD`: for each other node b and each kind, the number of marked objects
with the test {a, b} is that of the profile. 

### `sigP`

 The product of the σ_(q_j) over the checks j with home a. 

### `sgE`

 The number of marked clauses owned by a: the exponent of the sign in `WD`. 

### `WD_eq`

 `WD` written with the four tests, the product and the exponent named above. 

### `ok1_polyT`

 The first conjunct of `okD` is polynomial-time, for g and n in unary. 

### `ok2l_polyT`

 The test of one literal is polynomial-time. 

### `ok2_polyT`

 The second conjunct of `okD` is polynomial-time. 

### `ok3_polyT`

 The third conjunct of `okD` is polynomial-time, for g in unary. 

### `ok4_polyT`

 The fourth conjunct of `okD` is polynomial-time, for g in unary. 

### `sigP_polyT`

 «Multiplying powers of 2»: the product of the σ_(q_j) over the checks with home a is
polynomial-time. 

### `sgE_polyT`

 «Counting marks»: the number of marked clauses owned by a is polynomial-time, for g in unary. 

### `WD_polyT`

 The weight W_a(z_a) is polynomial-time, for g and n in unary. 

 ### The network of one profile 

### `netD_keeps`

 The lengths of the network of one profile are given in unary and its two functions are
polynomial-time, given `StCertRank` (⌈log C(t, μ)⌉ in unary, positions of strings in polynomial
time). 

 ### Admissible profiles 

### `tot_polyT`

 The sum Σ_a μ_(a,κ) is polynomial-time, for g in unary. 

### `totP_polyT`

 The sum Σ_({a,b}) μ_(a,b,κ) is polynomial-time, for g in unary. 

### `admD_polyT`

 The test «the profile y is admissible» is polynomial-time when g is given in unary and the other
arguments, the width k among them, are polynomial-time. 

### `stCertNet`

 Step 3, «The parameters»: «counting marks, multiplying powers of 2 and finding the position of a
string among those with as many ones take τ = n^O(1) operations, as condition (iii) requires». The
lengths of
the settings and of the labels of the network of one profile are given in unary, and W and f are
polynomial-time in the context (g and n in unary, the formula, the list of checks, the profile, and
the flag
that is true for the network of F, with the sign (-1)^q of the marked clauses owned by a, and false
for that of X) and their arguments. Needs the certificates of the binomial coefficients and of the
positions of strings. 

### `stCertAdm`

 Step 3, «Profiles»: the test «admissible» is polynomial-time jointly in all its arguments, for g
given in unary and k, n, n̄, M, the formula with the list of checks, the flag (F or X) and the
profile polynomial-time. 
