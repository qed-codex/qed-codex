---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/WeierstrassTwoTorsion/FglInvariant.lean",
  "declarations": [
    "Formalism.L2.Th1.A.fglLog"
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

## The logarithm of a Weierstrass formal group

[Theorem PHT.0232](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.A.fglLog/)

Let $K$ be a field of characteristic zero and $W$ any Weierstrass curve over $K$. Let $F_W(X,Y)$ be its formal group law in the parameter $t=-x/y$ at the identity, let $\omega_W(t)\,dt$ be its normalized invariant differential, and put $$\log_W(t)=\int_0^t\omega_W(s)\,ds,\qquad \exp_W=\log_W^{-1}$$ as formal power series under composition. Then $$\log_W(F_W(X,Y))=\log_W(X)+\log_W(Y),$$ $$F_W(X,Y)=\exp_W\bigl(\log_W(X)+\log_W(Y)\bigr).$$
