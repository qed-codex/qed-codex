---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermRepUnram.lean",
  "declarations": [
    "GlobalTheory.hermRepUnram"
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

## Representation by positive binary Hermitian forms

[Theorem ALG.1571](https://andrewodesky.com/rh/lean/GlobalTheory.hermRepUnram/)

Let $K$ be a totally complex number field with an involution $a\mapsto\bar a$ satisfying $\varphi(\bar a)=\overline{\varphi(a)}$ for every embedding $\varphi:K\hookrightarrow\mathbb C$. Assume that for every maximal ideal $\mathfrak p\subset\mathcal O_K$ there is $\theta\in\mathcal O_K$ with $\theta-\bar\theta\notin\mathfrak p$. If $a,b,n\in K$ are fixed by the involution and satisfy $$\Re\varphi(a)>0,\qquad\Re\varphi(b)>0,\qquad\Re\varphi(n)>0$$ for every embedding $\varphi$, there exist $s,t\in K$ such that $$a s\bar s+b t\bar t=n.$$
