---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/AdmHom.lean",
  "declarations": [
    "UpperTheory.V.Loc.isCrys_isDR_internalHom"
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

## Crystalline and de Rham properties pass through an equivariant pairing

[Theorem PHT.0300](https://andrewodesky.com/rh/lean/UpperTheory.V.Loc.isCrys_isDR_internalHom/)

Let $\ell$ be prime and $\phi:G\to G_{\mathbb Q_\ell}$ a group homomorphism that is an open embedding of topological groups. Let $A$ be a commutative $\mathbb Q_\ell$-algebra. Let $V,V',W$ be $A$-modules, finite-dimensional over $\mathbb Q_\ell$, with compatible scalar structures and their $\mathbb Q_\ell$-vector-space topologies; assume their additive groups are topological groups and multiplication by each element of $A$ is continuous. Let $\rho,\rho',\pi$ be continuous $A$-linear representations of $G$ on $V,V',W$, respectively.

Suppose there is an injective $\mathbb Q_\ell$-linear map $$b:W\longrightarrow\operatorname{Hom}_{\mathbb Q_\ell}(V,V')$$ satisfying $$b(\pi(g)w)(\rho(g)v)=\rho'(g)(b(w)(v)).$$ If $\rho,\rho'$ are crystalline, then $\pi$ is crystalline. If $\rho,\rho'$ are de Rham, then $\pi$ is de Rham. These period conditions are taken relative to $\phi$.
