---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/Assembly.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.AreaMultiplicity.full",
    "GroundTheory.Heights₂.Heights.ChartNorm.full",
    "GroundTheory.Heights₂.Heights.ComplexSets.DiscriminantCover.full",
    "GroundTheory.Heights₂.Heights.ComplexSets.FiniteProjectionsGeneric.full",
    "GroundTheory.Heights₂.Heights.CutOffDominated.full",
    "GroundTheory.Heights₂.Heights.IndefiniteRowSideFullHecke.ComplexSets.PolySublevel.full",
    "GroundTheory.Heights₂.Heights.LeadBlockGaussTail.full",
    "GroundTheory.Heights₂.Heights.NormFormEmbeddings.full",
    "GroundTheory.Heights₂.Heights.ProjectionFormula.full",
    "GroundTheory.Heights₂.Heights.VarietySlabMeasure.full"
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

## Dominated convergence for cutoff sheet integrals

[Theorem AG.1464](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.CutOffDominated.full/)

Let $J\subset\mathbb C[x_1,\ldots,x_n]$ be prime with $\dim V(J)=d$, and let $A:\mathbb C^n\to\mathbb C^d$ induce an injective finite map on coordinate rings. Let $P\in\mathbb C[y_1,\ldots,y_d]\setminus\{0\}$, let $f:\mathbb C^n\to\mathbb R$ be continuous on $V(J)$, and let $\psi_1,\ldots,\psi_d$ be real functions smooth near $V(J)$. For local holomorphic inverse branches $s$ of $A|_{V(J)}$, define the sheet integral $$I(f;\psi)=\int_{\mathbb C^d}\sum_{x\in V(J),\ Ax=y}f(x)\,\mathcal M(\psi_1\circ s,\ldots,\psi_d\circ s)(y)\,dy,$$ where $s(y)=x$, a point with no local sheet contributes zero, and $$\mathcal M(\eta_1,\ldots,\eta_d)=\left(\frac2\pi\right)^d\operatorname{Re}\sum_{S\subseteq\{1,\ldots,d\}}(-1)^{d-|S|}\det\left(\sum_{i\in S}\left[\frac{\partial^2\eta_i}{\partial z_a\partial\overline z_b}\right]_{a,b}\right).$$ Assume that the analogous density with absolute values around each summand is integrable.

Let $\chi_k:\mathbb C^n\to\mathbb R$ be measurable, $0\le\chi_k\le1$ everywhere, with $\chi_k(x)\to1$ for every $x\in V(J)$ such that $P(Ax)\ne0$. Then $$I(\chi_kf;\psi)\longrightarrow I(f;\psi).$$

## Generic finite linear projections

[Theorem AG.1135](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ComplexSets.FiniteProjectionsGeneric.full/)

Let $J\subseteq\mathbb C[x_1,\ldots,x_n]$ be prime and suppose $\dim\mathbb C[x]/J=d$. Call $A\in M_{d,n}(\mathbb C)$ a finite projection if the homomorphism $$\mathbb C[t_1,\ldots,t_d]\longrightarrow\mathbb C[x]/J,\qquad t_i\longmapsto\sum_j A_{ij}x_j,$$ is injective and makes the target a finite module over the source. Then:

1. A nonempty Zariski open subset of $M_{d,n}(\mathbb C)$ consists of finite projections.
2. If $D\subseteq\{A:AA^*=I_d\}$ is dense in that set for the usual topology, then $D$ contains a finite projection.
3. For every finite family $F_1,\ldots,F_m\in U(n)$ there is $U\in U(n)$ such that every matrix obtained by selecting any ordered $d$ distinct rows of any $F_kU$ is a finite projection.

## Power bounds for polynomial sublevel volumes

[Theorem AG.1187](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.ComplexSets.PolySublevel.full/)

Let $d\ge0$, let $Q\in\mathbb C[z_1,\ldots,z_d]$ be nonzero, and let $R>0$. There exist $C,\alpha>0$ such that, for every $0<\eta\le1$, $$\mathcal H^{2d}\{z\in\mathbb C^d:\|z\|<R,\ |Q(z)|\le\eta\}\le C\eta^\alpha.$$ Here $\mathcal H^{2d}$ is $2d$-dimensional Hausdorff measure for the Euclidean metric.

## The area formula with fibre multiplicities

[Theorem AG.1275](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.AreaMultiplicity.full/)

Let $E,F$ be finite-dimensional real inner product spaces of the same dimension $k\ge0$, equipped with their Borel measurable structures. Let $A\subseteq E$ be measurable, let $f:E\to F$, and suppose that for every $x\in A$ the continuous real-linear map $L_x:E\to F$ is a derivative of $f$ within $A$ at $x$. Write $\mathcal H^k$ for $k$-dimensional Hausdorff measure and $L_x^*$ for the adjoint. Then, as nonnegative extended integrals, $$\int_A\sqrt{\det(L_x^*L_x)}\,d\mathcal H^k(x)=\int_F\#\{x\in A:f(x)=y\}\,d\mathcal H^k(y).$$ Infinite fibres have cardinality $+\infty$ in the integrand.

## Factorization of a norm form over an algebraic closure

[Theorem ALG.1321](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NormFormEmbeddings.full/)

Let $K$ be an infinite field, let $L/K$ be a finite separable extension, and let $\Omega$ be an algebraically closed field supplied with a $K$-algebra structure. Given $n\ge0$ and $\eta_1,\ldots,\eta_n\in L$, choose a $K$-basis of $L$ and let $M_i$ be the matrix of multiplication by $\eta_i$. Define $$N_{\eta}(X_1,\ldots,X_n)=\det\!\left(\sum_{i=1}^nX_iM_i\right)\in K[X_1,\ldots,X_n].$$ After extending coefficients to $\Omega$, $$N_{\eta}(X)=\prod_{\sigma:L\hookrightarrow\Omega\,/K}\left(\sum_{i=1}^n X_i\sigma(\eta_i)\right).$$

## Volume of a holomorphic graph from coordinate projections

[Theorem AG.1428](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ProjectionFormula.full/)

Let $d,m,n\ge0$ and fix an identification $\mathbb C^n=\mathbb C^d\oplus\mathbb C^m$. Let $\Omega\subset\mathbb C^d$ be open, let $F:\mathbb C^d\to\mathbb C^m$ be holomorphic on $\Omega$, and let $B\subset\mathbb C^n$ be measurable. Put $$S=\{(z,F(z)):z\in\Omega\}\cap B.$$ For any orthonormal basis $b_1,\ldots,b_n$ of $\mathbb C^n$ and any $d$-element subset $I\subset\{1,\ldots,n\}$, write $p_I(z)=(\langle b_i,z\rangle)_{i\in I}$ and $N_I(x)=\#(S\cap p_I^{-1}(x))$, allowing infinite values. With $\mathcal H^{2d}$ the $2d$-dimensional Hausdorff measure, $$\mathcal H^{2d}(S)=\sum_{|I|=d}\int_{\mathbb C^I}N_I(x)\,d\mathcal H^{2d}(x).$$

## Holomorphic branches away from a projection discriminant

[Theorem AG.1497](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ComplexSets.DiscriminantCover.full/)

Let $J\subset\mathbb C[x_1,\ldots,x_n]$ be prime with $\dim(\mathbb C[x]/J)=d$, and let $A:\mathbb C^n\to\mathbb C^d$ be linear. Suppose the induced map $\mathbb C[y_1,\ldots,y_d]\to\mathbb C[x]/J$ is injective and finite. Write $X=V(J)$ and let $D$ be the dimension of $\mathbb C(y)\otimes_{\mathbb C[y]}\mathbb C[x]/J$ over $\mathbb C(y)$.

There is a nonzero polynomial $P\in\mathbb C[y]$ such that, whenever $P(y)\ne0$, the fiber $X\cap A^{-1}(y)$ is finite of cardinality $D$. For every $x$ in that fiber there are open neighborhoods $U\subset\mathbb C^d$ of $y$ and $V\subset\mathbb C^n$ of $x$, and a holomorphic map $g:U\to\mathbb C^n$, with $$g(y)=x,\qquad Ag(w)=w\ (w\in U),\qquad X\cap V=g(U).$$

## Power decay of the measure of a thin algebraic slab

[Theorem AG.1524](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.VarietySlabMeasure.full/)

Let $n,d\ge0$, let $J\subset\mathbb C[x_1,\ldots,x_n]$ be prime with $\dim(\mathbb C[x]/J)\le d$, and take $u\in\mathbb C^n$ such that $\ell_u=\sum_j u_jx_j\notin J$. For every $R\in\mathbb R$, there are $C,\alpha>0$ such that, for $0<\varepsilon\le1$, $$\mathcal H^{2d}\!\left(\left\{z\in V(J):\|z\|_2\le R,\ \left|\sum_j u_jz_j\right|\le\varepsilon\right\}\right)\le C\varepsilon^\alpha.$$ Here $\mathcal H^{2d}$ is Hausdorff measure for the Euclidean metric on $\mathbb C^n$.

## A Chow form as a determinant on an incidence chart

[Theorem AG.1530](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ChartNorm.full/)

Let $F$ have characteristic zero, let $n,e\ge0$, and let $I\subseteq F[x_1,\ldots,x_n]$ be a homogeneous prime defining a nonempty integral projective variety. Let $f$ be its Chow form in $e+1$ blocks of $n$ coefficients, in the sense of ([Existence of a Chow form](https://andrewodesky.com/rh/lean/GlobalTheory.ChowExists.exists_isChowFormInt/)). Write $S=F[a_{ij}:1\le i\le e,1\le j\le n]$, let $\mathfrak p$ be a prime ideal of $S$ that is zero or generated by a prime element, and put $R=S_{\mathfrak p}$. For $u\in F^n$, put $\ell_u(x)=\sum_j u_jx_j$ and let $f_u\in S$ denote substitution of $u$ in the first block of $f$.

Fix $t\in F^n$ with $f_t\notin\mathfrak p$ and form the incidence algebra $$A=R[x_1,\ldots,x_n]/\bigl(I,\ \ell_t-1,\ \sum_j a_{ij}x_j\ (1\le i\le e)\bigr).$$ Then for every $u\in F^n$, $$f_u=f_t\det_R\bigl(m_{\ell_u}:A\to A\bigr)\quad\text{in }R,$$ where $m_{\ell_u}$ is multiplication by the image of $\ell_u$.

## A Gaussian matrix integral with polynomial tail decay

[Theorem AG.1749](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.LeadBlockGaussTail.full/)

Let $m\ge1$ and $k\ge0$ be integers. For $\Pi\in M_{m,m+k}(\mathbb C)$ let $\Pi_0$ be its first $m$ columns, let $e_1=(1,0,\ldots,0)\in\mathbb C^{m+k}$, and put $$\|\Pi\|_F^2=\sum_{i=1}^m\sum_{j=1}^{m+k}|\Pi_{ij}|^2.$$ There is $C=C(m,k)\in\mathbb R$ such that, for every $r\in\mathbb R$, $$\int_{M_{m,m+k}(\mathbb C)}e^{-\|\Pi\|_F^2}\,\mathbf1_{\{\|\Pi(re_1)\|_2<1\}}\,|\det\Pi_0|^2\,d\Pi \le\max\left\{0,\frac{C}{(1+r^2)^{m+1}}\right\}.$$ Here $d\Pi$ is the product of the usual Lebesgue measures on the complex matrix entries, and the integral is the nonnegative extended integral.
