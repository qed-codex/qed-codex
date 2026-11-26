---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/H2EquivOfTorsionCharacter.lean",
  "declarations": [
    "GlobalTheory.TateTop.exists_gen_all"
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

## A single cocycle generator for all finite prime-power levels

[Theorem GC.1513](https://andrewodesky.com/rh/lean/GlobalTheory.TateTop.exists_gen_all/)

Let $\ell$ be prime, let $G$ be a group with a topology for which multiplication is continuous, and let $\chi:G\to\mathbb Z_\ell^\times$ be a homomorphism whose underlying $\mathbb Z_\ell$-valued function is continuous. For a finite $\mathbb Z_\ell$-module $M$, call $z:G^2\to M$ a cocycle if it is locally constant and $$\chi(g)z(h,k)-z(gh,k)+z(g,hk)-z(g,h)=0.$$ For a locally constant $b:G\to M$, put $\delta b(g,h)=\chi(g)b(h)-b(gh)+b(g)$.

Say $c:G^2\to\mathbb Z_\ell$ generates level $r$ if, for every finite $M$ killed by $\ell^r$, all functions $c\,x$ with $x\in M$ are cocycles, every cocycle has the form $c\,x+\delta b$, and $c\,x=\delta b$ implies $x=0$. Assume that for every $r\ge0$ there is a function generating level $r+1$. Then there is a single function $c$ generating every level $r\ge0$.
