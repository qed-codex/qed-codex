---
{
  "module": "src/Formalism/TorsionNormIteration/LubinTateExample.lean",
  "declarations": [
    "Formalism.LT.funEqGroup"
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

## An integral addition law from a Frobenius functional equation

[Theorem PHT.0972](https://andrewodesky.com/rh/lean/Formalism.LT.funEqGroup/)

Let $K$ be an ultrametric normed field of characteristic zero. Let $p$ be prime, let $h$ be a positive integer, put $q=p^h$, and let $\sigma:K\to K$ be a ring endomorphism such that $|p|<1$ and $$|\sigma(a)-a^q|\le|p|\qquad(|a|\le1).$$ Let $f(T)\in K[[T]]$ satisfy $f(0)=0$, $[T]f=1$, and suppose every coefficient of $$f(T)-p^{-1}\sigma(f)(T^q)$$ has norm at most one, where $\sigma$ acts on coefficients. There is $F(X,Y)\in K[[X,Y]]$ with zero constant coefficient, all coefficients of norm at most one, and $$f(F(X,Y))=f(X)+f(Y).$$
