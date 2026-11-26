---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/SecondCoefficientNorms/PhNormFromDatum.lean",
  "declarations": [
    "Formalism.L2.Th1.C.ptClosure"
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

## Integral points and scalars for a formal group law

[Theorem ALG.0604](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.C.ptClosure/)

Let $K$ be a field, $R\subseteq K$ a subring, and $l,e\in K[[X]]$ satisfy $$l(0)=e(0)=0,\qquad [X]l=1,\qquad e(l(X))=l(e(X))=X.$$ Assume $F(X,Y)=e(l(X)+l(Y))$ has coefficients in $R$. For any set of variables, series with coefficients in $R$ and zero constant term are closed under $(x,y)\mapsto e(l(x)+l(y))$. They are also closed under $x\mapsto e(a\,l(x))$ whenever the one-variable series $[a](X)=e(a\,l(X))$ has coefficients in $R$.

The set $$\{a\in K:[a](X)\in R[[X]]\}$$ contains $0,1,-1$ and is closed under addition and multiplication.
