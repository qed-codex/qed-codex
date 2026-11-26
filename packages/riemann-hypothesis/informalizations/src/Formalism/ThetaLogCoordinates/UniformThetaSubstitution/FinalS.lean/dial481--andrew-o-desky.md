---
{
  "module": "src/Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FinalS.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.G7.Top.dworkMv",
    "Formalism.InvariantFactorPaths.G7.Top.lemmaOne",
    "Formalism.InvariantFactorPaths.G7.Top.lemmaTwo"
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

## A bivariate series is a logarithm product modulo integral coefficients

[Theorem PHT.0715](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.lemmaTwo/)

Let $K$ be a complete ultrametric normed field of characteristic zero, let $p>2$ be prime, and let $\sigma:K\to K$ be a ring endomorphism. Assume $$|p|=p^{-1},\qquad |K^\times|\subseteq p^{\mathbb Z},\qquad|\sigma(a)-a^p|\le p^{-1}\quad(|a|\le1).$$ Put $\ell(T)=\sum_{j\ge0}T^{p^{2j}}/p^j$, and let $F(X,Y)$ have zero constant term, coefficients of norm at most $1$, and $\ell(F(X,Y))=\ell(X)+\ell(Y)$. Let $H(X,Y)\in XYK[[X,Y]]$. If both series $$H(F(X,Y),Z)-H(X,Z)-H(Y,Z),$$ $$H(Z,F(X,Y))-H(Z,X)-H(Z,Y)$$ have all coefficients of norm at most $1$, then there are $\beta\in K$ and $R\in K[[X,Y]]$ with all coefficients of norm at most $1$ such that $$H(X,Y)=\beta\ell(X)\ell(Y)+R(X,Y).$$

## A multivariable Dwork criterion over an ultrametric field

[Theorem PHT.1111](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.dworkMv/)

Let $K$ be an ultrametric normed field of characteristic zero, $p$ a prime with $|p|=p^{-1}$, and $\sigma:K\to K$ a ring endomorphism satisfying $$|\sigma(a)-a^p|\le p^{-1}\qquad(|a|\le1).$$ For finitely many variables $X_i$ and $\Psi\in K[[X_i]]$ with zero constant coefficient, $$\exp\Psi\in\mathcal O_K[[X_i]]\quad\Longleftrightarrow\quad\Psi^\sigma(X_i^p)-p\Psi(X_i)\in p\mathcal O_K[[X_i]],$$ where $\mathcal O_K=\{a:|a|\le1\}$ and $\Psi^\sigma$ is obtained by applying $\sigma$ to each coefficient.

## Decomposition of a series with integral formal coboundary

[Theorem PHT.0689](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.G7.Top.lemmaOne/)

Let $K$ be a complete ultrametric normed field of characteristic zero, $p>2$ a prime, and $\sigma:K\to K$ a ring homomorphism. Assume $|p|=p^{-1}$, every nonzero element has norm $p^a$ for some $a\in\mathbb Z$, and $|\sigma(x)-x^p|\le p^{-1}$ for $|x|\le1$. Define $$L(X)=\sum_{j\ge0}\frac{X^{p^{2j}}}{p^j},\qquad G(X)=\sum_{j\ge0}\frac{X^{p^{2j+1}}}{p^{j+1}}.$$ Let $F\in K[[X,Y]]$ have zero constant term, coefficients of norm at most one, and satisfy $L(F(X,Y))=L(X)+L(Y)$. If $f\in K[[X]]$ has zero constant term and every coefficient of $$f(F(X,Y))-f(X)-f(Y)$$ has norm at most one, there are $\alpha,\beta\in K$ and $R\in K[[X]]$ such that $$|\alpha|\le1,\qquad |[X^n]R|\le1\ (n\ge0),\qquad f=\alpha G+\beta L+R.$$
