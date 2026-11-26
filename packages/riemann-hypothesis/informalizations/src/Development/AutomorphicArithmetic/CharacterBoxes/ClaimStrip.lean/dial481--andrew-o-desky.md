---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean",
  "declarations": [
    "Claim.prim_reflect"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Reflection of primitive Dirichlet zeros

[Theorem ANT.1738](https://andrewodesky.com/rh/lean/Claim.prim_reflect/)

Let $M\ge1$ be an integer and let $\psi$ be a primitive complex Dirichlet character modulo $M$. Primitive means that $M$ is the least positive divisor of $M$ from which $\psi$ is induced, where induction extends a character from that divisor by setting its values to zero on integers not coprime to $M$. Write $L(s,\psi)$ for the meromorphic continuation of $\sum_{n\ge1}\psi(n)n^{-s}$ from $\Re s>1$, and put $\overline\psi(n)=\overline{\psi(n)}$ for every integer $n$. For $s\in\mathbb C$, $$0<\Re s<1,\qquad L(s,\psi)=0 \quad\Longrightarrow\quad L(1-s,\overline\psi)=0.$$ On integers coprime to $M$, $\overline\psi(n)=\psi(n)^{-1}$; both characters vanish on the remaining integers.
