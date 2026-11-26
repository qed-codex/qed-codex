---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsPrimitiveCharacterTwistStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_primitive_character_twist"
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

## A primitive prime-power character in a prescribed residue component

[Theorem ANT.0573](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_primitive_character_twist/)

Let $\ell$ be an odd prime, let $\varphi$ be a Dirichlet character modulo $\ell$ with values in $\overline{\mathbb Q}_\ell$, and let $e\ge0$ and $k\ge1$ be integers. Let $\zeta\in\overline{\mathbb Q}_\ell$ have exact order $\ell^k$. There is a primitive Dirichlet character $\psi$ modulo $\ell^{k+1}$ such that $$\psi^{-1}(1+\ell)=\zeta.$$ For every $b\in(\mathbb Z/\ell^{k+1}\mathbb Z)^\times$ with $b^{\ell-1}=1$, it also satisfies $$\left|\psi^{-1}(b)-\widetilde b^{\,e}\varphi(\widetilde b\bmod\ell)\right|_\ell<1,$$ where $\widetilde b\in\{0,\ldots,\ell^{k+1}-1\}$ is the integer representative of $b$.
