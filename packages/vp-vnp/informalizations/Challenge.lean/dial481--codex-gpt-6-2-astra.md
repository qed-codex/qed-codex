---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Five targets for arithmetic circuits over fields

AI drafted this autoinformalization from the original source. It is open for mathematical review.

The challenge gives five statements in the namespace `Solution`, with `sorry` in each proof position. Four refer to propositions in `Statement.lean`; the fifth spells out a lower bound for the permanent over the reals. In this model a circuit is an ordered list of polynomials. A variable or a scalar counts as a gate, as does a sum or product of two earlier entries. [Challenge.lean lines 6–33](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L6-L33) · [Statement.lean lines 20–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L20-L31)

**Two quantitative bounds.** There is a constant $c>0$ such that all sufficiently large $m$ require more than $m^{c(\log_2 m)^{1/3}}$ gates for the Hamiltonian-cycle polynomial. The threshold may depend on the characteristic. The permanent has the same bound in characteristic different from two. The approximate version allows coefficients in Laurent series: for every monomial the coefficient at parameter degree zero must be correct, and every negative-degree coefficient must vanish. [Statement.lean lines 33–46](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L33-L46) · [Statement.lean lines 48–60](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L48-L60)

**Two class statements.** Over each field, VP is a proper subset of VNP. In addition, some VNP family lies outside `VPBar`, the class defined using polynomially bounded approximating circuits. The separate real-permanent statement asks for a positive $c$ and a threshold $m_0$ valid for all $m\ge m_0$ and all exact circuit sizes. [Statement.lean lines 75–96](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean#L75-L96) · [Challenge.lean lines 23–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L23-L31)

I read the challenge and the cited definitions. I did not build the project or verify a circuit lower bound independently.
