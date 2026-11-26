---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/HenselStatementStatement.lean",
  "declarations": [
    "GlobalTheory.T.HenselStatement"
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

## A quadratic equation in the fixed field of an involution

[Theorem PHT.1547](https://andrewodesky.com/rh/lean/GlobalTheory.T.HenselStatement/)

Let $L$ be a complete nontrivially normed field with ultrametric distance. Let $s:L\to L$ be a nonidentity ring involution preserving the norm. If $c,d\in L$ satisfy $$s(c)=c,\qquad s(d)=d,\qquad |c|<1,\qquad |d|\le1,$$ then there is $u\in L$ with $$s(u)=u,\qquad |u|\le1,\qquad d+u+cu^2=0.$$
