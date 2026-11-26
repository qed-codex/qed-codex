---
{
  "module": "src/PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/FinalTF.lean",
  "declarations": [
    "UpperTheory.Esk.finite_system_holds",
    "UpperTheory.Esk.multivariable_reproducing_formula_holds",
    "UpperTheory.Esk.s_LinTr",
    "UpperTheory.Esk.s_Sys"
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

## A trace formula from a finite-dimensional reproducing kernel

[Theorem ALG.0346](https://andrewodesky.com/rh/lean/UpperTheory.Esk.s_LinTr/)

Let $A$ be a set, $(Y,\nu)$ a finite measure space, $V\subseteq\mathbb C^A$ a finite-dimensional linear subspace, $T:V\to V$ linear, $K:Y\to V$, $e:Y\to A$, and $n:Y\to\mathbb R_{>0}$ measurable. Suppose $y\mapsto K(y)(a)$ is measurable for every $a\in A$, and $y\mapsto f(e(y))$ is measurable for every $f\in V$. Assume that for each $a$ there is $C_a\in\mathbb R$ with $$|K(y)(a)|\le C_an(y)\qquad(y\in Y),$$ and for each $f\in V$ there is $C_f\in\mathbb R$ with $$|f(e(y))|n(y)\le C_f\qquad(y\in Y).$$ If $$\int_YK(y)(a)f(e(y))\,d\nu(y)=f(a)\qquad(f\in V,\ a\in A),$$ then $y\mapsto(TK(y))(e(y))$ is measurable and bounded, and $$\operatorname{tr}(T)=\int_Y(TK(y))(e(y))\,d\nu(y).$$

## A reproducing formula on products of complex half-planes

[Theorem REP.0655](https://andrewodesky.com/rh/lean/UpperTheory.Esk.multivariable_reproducing_formula_holds/)

Put $P=\mathbb C\setminus\mathbb R$, with measure $d\mu(w)=d\operatorname{Re}(w)\,d\operatorname{Im}(w)/\operatorname{Im}(w)^2$. Let $I$ be finite and let $k_v\ge4$ be integers for $v\in I$. For $z,w\in P$ put $$q_k(z,w)=\begin{cases}\displaystyle\frac{k-1}{4\pi}\left(\frac{w-\overline w}{z-\overline w}\right)^k,&\operatorname{Im}(z)\operatorname{Im}(w)>0,\\0,&\operatorname{Im}(z)\operatorname{Im}(w)\le0.\end{cases}$$ Let $f:P^I\to\mathbb C$ be continuous and holomorphic in each variable separately. Suppose some real constant $C$ satisfies $$|f(z)|\prod_{v\in I}|\operatorname{Im}(z_v)|^{k_v/2}\le C\qquad(z\in P^I).$$ For every $z\in P^I$, the integrand below is integrable and $$\int_{P^I}\left(\prod_{v\in I}q_{k_v}(z_v,w_v)\right)f(w)\,\prod_{v\in I}d\mu(w_v)=f(z).$$

## Joint eigencharacters and traces of commuting operators

[Theorem ALG.0272](https://andrewodesky.com/rh/lean/UpperTheory.Esk.s_Sys/)

Let $V$ be a finite-dimensional complex vector space, $J$ any set, and $(T_j)_{j\in J}$ pairwise commuting endomorphisms of $V$. There are a finite set $S\subseteq\mathbb C^J$ and integers $m(s)\ge1$ for $s\in S$ such that $$s\in S\ \Longleftrightarrow\ \exists v\ne0\ \forall j,\ T_jv=s(j)v,\qquad\sum_{s\in S}m(s)=\dim_{\mathbb C}V.$$ For every finite list $j_1,\ldots,j_t$ of elements of $J$, $$\operatorname{tr}(T_{j_1}\cdots T_{j_t})=\sum_{s\in S}m(s)s(j_1)\cdots s(j_t).$$ Empty products are identities.

## Trace congruences force a nearby simultaneous eigencharacter

[Theorem ALG.0585](https://andrewodesky.com/rh/lean/UpperTheory.Esk.finite_system_holds/)

Let $\nu:\mathbb C\to\mathbb R_{\ge0}$ be a multiplicative valuation, let $\ell$ be prime with $\nu(\ell)<1$, and let $V,V'$ be finite-dimensional complex vector spaces. Let $J$ be a set and let $(T_j)_{j\in J}$ and $(T'_j)_{j\in J}$ be commuting families of endomorphisms of $V$ and $V'$, respectively. Fix a finite $L\subseteq J$ and $\epsilon,\rho\ge0$ with $\rho<1$ and $$\epsilon<\nu(d)\qquad(1\le d\le\dim_{\mathbb C}V).$$ For every finite word $W$ in $J$ and every integer $r\ge1$ for which each $j\in L$ occurs at least $r$ times in $W$, suppose $$\nu\!\left(\operatorname{tr}T_W\right)\le1,\quad\nu\!\left(\operatorname{tr}T'_W\right)\le1,\quad \nu\!\left(\operatorname{tr}T_W-\operatorname{tr}T'_W\right)\le\max\{\epsilon,\rho^r\},$$ where $T_W$ and $T'_W$ are the products in the order of the word. If $0\ne f\in V$ satisfies $T_jf=s_jf$ for all $j$ and $\nu(s_j)=1$ for $j\in L$, there are $0\ne f'\in V'$ and $s'_j\in\mathbb C$ with $$T'_jf'=s'_jf'\quad(j\in J),\qquad\nu(s'_j-s_j)<1\quad(j\in J).$$
