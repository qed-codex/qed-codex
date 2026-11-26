---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/HeckeCharLocalComponentExistsUniqueUnitary.lean",
  "declarations": [
    "GlobalTheory.HeckeComp.main"
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

## Unique finite local component of a Hecke character

[Theorem ANT.1684](https://andrewodesky.com/rh/lean/GlobalTheory.HeckeComp.main/)

Let $E$ be a number field, $\chi$ a Hecke character of $E$, and $w$ a finite place. Let $\chi_w^{\mathrm{rat}}:E^\times\to\mathbb C^\times$ be the character obtained by evaluating $\chi$ on the idele with $w$-component equal to the given element and all other components equal to one. There is a unique smooth character $\xi:E_w^\times\to\mathbb C^\times$ such that $$\xi(x)=\chi_w^{\mathrm{rat}}(x)\qquad(x\in E^\times).$$ Here smooth means that the kernel is open. If $\chi$ is unitary, then $|\xi(y)|=1$ for every $y\in E_w^\times$.
