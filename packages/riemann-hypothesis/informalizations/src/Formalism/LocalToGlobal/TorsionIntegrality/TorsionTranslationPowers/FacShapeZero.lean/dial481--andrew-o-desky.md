---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/TorsionTranslationPowers/FacShapeZero.lean",
  "declarations": [
    "Formalism.L2.Th1.E.parSumTwo"
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

## A parallelogram identity forces constancy on a finite group

[Theorem ALG.0806](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.E.parSumTwo/)

Let $A$ be a finite abelian group and let $M,m:A\to\mathbb R$. Suppose that for every $P\in A$ and every $Q\ne0$, $$M(P+Q)+M(P-Q)-2M(P)=2m(Q).$$ Then $m(Q)=0$ for every $Q\ne0$, and $M(P)=M(0)$ for every $P\in A$.
