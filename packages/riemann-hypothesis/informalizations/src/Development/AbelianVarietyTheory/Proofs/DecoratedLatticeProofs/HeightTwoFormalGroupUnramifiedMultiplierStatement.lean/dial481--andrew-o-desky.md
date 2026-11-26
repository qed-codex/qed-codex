---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HeightTwoFormalGroupUnramifiedMultiplierStatement.lean",
  "declarations": [
    "GlobalTheory.T.heightTwo_formalGroup_unramified_multiplier"
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

## Integral comparison with a height-two formal logarithm

[Theorem PHT.0557](https://andrewodesky.com/rh/lean/GlobalTheory.T.heightTwo_formalGroup_unramified_multiplier/)

Let $K$ be a complete ultrametric normed field of characteristic zero, let $\ell>2$ be prime, and let $\sigma:K\to K$ be a ring homomorphism. Assume $$|\ell|<1,\quad |x|<1\Longrightarrow |x|\le|\ell|,\quad |\sigma x|=|x|,$$ $$|x|\le1\Longrightarrow|\sigma x-x^\ell|<1.$$ Assume also that every monic positive-degree polynomial with coefficients in $O=\{x:|x|\le1\}$ has a root modulo the maximal ideal: for every such polynomial $P$, some $x\in O$ satisfies $|P(x)|<1$. Let $f,e\in K[[T]]$ satisfy $f(0)=e(0)=0$, $f'(0)=1$, and $f\circ e=e\circ f=T$. Assume $f'\in O[[T]]$ and the formal group law $$F(X,Y)=e(f(X)+f(Y))$$ has coefficients in $O$. For $a\in K$ put $[a]_F(T)=e(af(T))$. Suppose $w\in K$ satisfies $$[w]_F\in O[[T]],\qquad\sigma^2w=w,\qquad|\sigma w-w|=1,$$ and some $0\le n\le\ell^2$ has $|[T^n][\ell]_F|=1$. There is $\epsilon\in K$ with $|\epsilon|=1$ such that $$e\left(\epsilon\sum_{j\ge0}\frac{T^{\ell^{2j}}}{\ell^j}\right)\in O[[T]].$$
