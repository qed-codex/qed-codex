---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/IsCrysOfInertia.lean",
  "declarations": [
    "UpperTheory.V.Loc.crUnr"
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

## Crystallinity from a scalar cyclotomic inertia action

[Theorem PHT.0319](https://andrewodesky.com/rh/lean/UpperTheory.V.Loc.crUnr/)

Let $\ell$ be prime, $G$ a topological group, and $\varphi:G\hookrightarrow G_{\mathbb Q_\ell}$ an open embedding of topological groups. Let $A$ be a commutative $\mathbb Q_\ell$-algebra, also a $\mathbb Z_\ell$-algebra compatibly, and $V$ an $A$-module finite-dimensional over $\mathbb Q_\ell$. Give $V$ its $\mathbb Q_\ell$-module topology, with continuous addition and continuous multiplication by each element of $A$. Let $\rho:G\to\operatorname{Aut}_A(V)$ have continuous action. If, for some $w\in\mathbb Z$, $$\rho(g)v=\chi_\ell(\varphi(g))^w v\qquad\bigl(\varphi(g)\in I_\ell,\ v\in V\bigr),$$ then $$\dim_{\mathbb Q_\ell}D_{\mathrm{cris},\varphi}(V)=[G_{\mathbb Q_\ell}:\varphi(G)I_\ell]\dim_{\mathbb Q_\ell}V.$$ Here $I_\ell$ is inertia, $\chi_\ell$ is the $\ell$-adic cyclotomic character mapped to $A^\times$, and $D_{\mathrm{cris},\varphi}(V)=(V\otimes_{\mathbb Q_\ell}B_{\mathrm{cris}})^G$ for the action through $\varphi$ on the period ring. The displayed dimension equality defines crystallinity relative to $\varphi$ here.
