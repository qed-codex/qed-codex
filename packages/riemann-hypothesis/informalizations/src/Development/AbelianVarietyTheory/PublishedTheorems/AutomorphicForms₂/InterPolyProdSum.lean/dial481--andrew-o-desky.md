---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean",
  "declarations": [
    "GlobalTheory.GoodMetric.GoodBound",
    "GlobalTheory.GoodMetric.HasChernIntegral",
    "GlobalTheory.GoodMetric.IsGood",
    "GlobalTheory.GoodMetric.IsGraded",
    "GlobalTheory.GoodMetric.IsHoloChart",
    "GlobalTheory.GoodMetric.IsMetricOn",
    "GlobalTheory.GoodMetric.antisymm",
    "GlobalTheory.GoodMetric.chernRoots",
    "GlobalTheory.GoodMetric.chernTop",
    "GlobalTheory.GoodMetric.chernTopPart",
    "GlobalTheory.GoodMetric.fibrePoint",
    "GlobalTheory.GoodMetric.rootDiscr",
    "GlobalTheory.ProjVar.Var.interPoly"
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

## Good Hermitian metrics and signed Chern integrals

[Definition / hypothesis AG.D037](https://andrewodesky.com/rh/lean/GlobalTheory.GoodMetric.IsMetricOn/)

Let $F$ be a field with an embedding $\sigma:F\hookrightarrow\mathbb C$, and let $X/F$ be smooth, geometrically integral and projective of dimension $d\in\mathbb N$. Fix a finite index set $I$, ranks $m_i\in\mathbb N$, and a rational frame system $E$ of type $0$ as in ([Rational frame systems and flag refinements](https://andrewodesky.com/rh/lean/GlobalTheory.FlagBundle.Fr/)). For a complex point $y\in X_\sigma(\mathbb C)$, write $\underline y$ for its underlying point of $X$.

Use total rational-function evaluation $\operatorname{val}_y$, algebraic coordinate charts and the chart-supremum construction of measures from ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)), with base ring $F$. Smooth real functions have the local meaning through finitely many regular functions specified under “Hermitian metrics” in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)).

**Metrics in rational frames.** Choose functions $$H_A:X_\sigma(\mathbb C)\longrightarrow\prod_{i\in I}\operatorname{Mat}_{m_i}(\mathbb C),\qquad A\in\prod_{i\in I}\operatorname{Mat}_{m_i}(F(X)).$$ Let $O\subseteq X$ be open, and put $O_\sigma=O(\mathbb C)$. A smooth positive Hermitian metric on $E$ over $O_\sigma$ means that, for every $y\in O_\sigma$ and every $A\in E_{\underline y}$, each matrix $H_{A,i}(y)$ is positive definite, and the real and imaginary parts of every entry of $H_{A,i}$ are smooth at $y$ in the preceding local sense. For every $A,A'\in E_{\underline y}$, require $$H_{A',i}(y)=T_i(y)H_{A,i}(y)T_i(y)^*,\qquad T_i(y)=\operatorname{val}_y(A'_iA_i^{-1}),$$ where evaluation is entrywise and $*$ is conjugate transpose.

**Connection and curvature.** In coordinates on $\mathbb C^d$, use the entrywise Wirtinger operators $$\partial_a=\tfrac12(D_{e_a}-iD_{ie_a}),\qquad \bar\partial_a=\tfrac12(D_{e_a}+iD_{ie_a}),$$ where $D_v$ applies the real Frechet derivative to $v$. A nonexistent real Frechet derivative is taken to be zero, and the inverse of a singular square matrix is zero. For a matrix-valued function $G$, put $$\Gamma_a(G)=(G^{\mathsf T})^{-1}(\partial_aG)^{\mathsf T},\qquad \Omega_{ab}(G)=-\bar\partial_b\Gamma_a(G).$$

**Good boundary growth.** Such a metric is good if the following holds at every $y\notin O_\sigma$. There are a homeomorphism $e:V\to T$ between open subsets of $X_\sigma(\mathbb C)$ and $\mathbb C^d$, with $y\in V$, and a subset $S\subseteq\{0,\ldots,d-1\}$ such that $$e_a(y)=0\quad(a\in S),\qquad V\setminus O_\sigma=\{x\in V:\ e_a(x)=0\text{ for some }a\in S\}.$$ For every regular function on any open subset of $X$, its pullback along $e^{-1}$ must be holomorphic where defined.

There are a frame $A\in E_{\underline y}$, a real number $c$ and $N\in\mathbb N$ such that all the following bounds hold on $O_\sigma$ sufficiently near $y$, with the same $c,N$ for every $i\in I$. For $z=e(x)$ set $$G_i(v)=H_{A,i}(e^{-1}(v)),\qquad L(z)=\sum_{a\in S}|\log|z_a||,\qquad w_a(z)=\begin{cases}|z_a|\,|\log|z_a||,&a\in S,\\1,&a\notin S.\end{cases}$$ For every $i\in I$, require $$|\det G_i(z)|^{-1}\le cL(z)^N.$$ For every entry $(j,k)$ of $G_i$, require $$|(G_i(z))_{jk}|\le cL(z)^N,$$ and, for every coordinate $a$, $$|(\Gamma_a(G_i)(z))_{jk}|w_a(z)\le c.$$ For every pair of coordinates $(a,b)$, require $$|(\Omega_{ab}(G_i)(z))_{jk}|w_a(z)w_b(z)\le c,$$ and $$|\bigl(\partial_a\Gamma_b(G_i)-\partial_b\Gamma_a(G_i)\bigr)(z)_{jk}|w_a(z)w_b(z)\le c.$$

**Chern densities and integrals.** Fix once a frame $A_y\in E_{\underline y}$ at each complex point. In an algebraic chart $e$ and at $y$ in its source, hold $A_y$ fixed while differentiating $$G_i^{,y}(v)=H_{A_y,i}(e^{-1}(v)).$$ For commuting indeterminates $Z_{ab}$ define $$\Omega_i^e(y;Z)=\sum_{a,b=0}^{d-1}\Omega_{ab}(G_i^{,y})(e(y))Z_{ab},\qquad C_{i,j}^e(y;Z)=[t^j]\det\bigl(I_{m_i}+t\Omega_i^e(y;Z)\bigr).$$ For a polynomial $Q$ in the $Z_{ab}$ put $$\operatorname{Top}_d Q=\sum_{w\in\mathfrak S_d}\operatorname{sgn}(w) \left[\prod_{a=0}^{d-1}Z_{a,w(a)}\right]Q.$$ For $R\in\mathbb R[c_{i,j}:i\in I,\ j\in\mathbb N]$, its real density in this chart is $$\rho_{R,e}(y)=\pi^{-d}\operatorname{Re}\operatorname{Top}_d\!\left(R\bigl(C_{i,j}^e(y;Z)\bigr)\right).$$ Apply the chart-supremum measure construction of ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)) to the chart densities $\max\{\varepsilon\rho_{R,e},0\}$ for each $\varepsilon\in\{1,-1\}$. Denote the resulting measures by $\mu_R^+$ and $\mu_R^-$.

Say that $R$ has Chern integral $t\in\mathbb R$ on $O_\sigma$ if both $\mu_R^+(O_\sigma)$ and $\mu_R^-(O_\sigma)$ are finite and their difference is $t$. In this case write $$\int_{O_\sigma}R(c(H))=\mu_R^+(O_\sigma)-\mu_R^-(O_\sigma)=t.$$ For a single bundle, $c_j(E,H)$ denotes the choice $R=c_{*,j}$. Empty sums and products are $0$ and $1$; in dimension zero the empty determinant is $1$ and $\operatorname{Top}_0 Q$ is the constant coefficient of $Q$.

## Rational frame systems and flag refinements

[Definition / hypothesis AG.D074](https://andrewodesky.com/rh/lean/GlobalTheory.FlagBundle.Fr/)

Let $F$ be a field and $Z$ an integral separated scheme of finite type over $F$, with function field $\Omega=F(Z)$. Regard every local ring $\mathcal O_{Z,z}$ as a subring of $\Omega$. Fix a finite index set $I$ and natural numbers $m_i,k_i$ for $i\in I$. All matrix indices start at zero.

**Rational frame systems.** For a subring $O\subseteq K$ of a field, define $P_k(O)$ to be the set of tuples $g=(g_i)_{i\in I}$ satisfying $$g_i\in\mathrm{GL}_{m_i}(K),\qquad (g_i)_{ab}\in O,\qquad (\det g_i)^{-1}\in O,$$ and $$(g_i)_{ab}=0\quad\text{whenever }a<k_i\text{ and }a<b.$$ A rational frame system of type $k$ on $Z$ is a family $$S_z\subseteq\prod_{i\in I}\mathrm{GL}_{m_i}(\Omega)$$ with the following local description: every point has an open neighbourhood $U$ and a fixed tuple $A$ of invertible matrices over $\Omega$ such that $$S_z=P_k(\mathcal O_{Z,z})A\qquad(z\in U).$$ Type $0$ gives unrestricted invertible changes of local frame and describes locally free sheaves of ranks $m_i$. Type $m=(m_i)_i$ gives lower triangular changes of frame.

**Refinements.** Let $Y$ be another integral separated scheme of finite type over $F$, with function field $\Omega'$. Let $S'$ be a frame system of type $k'$ on $Y$. A refinement from $S$ to $S'$ consists of an $F$-embedding $\phi:\Omega\hookrightarrow\Omega'$ and a dominant $F$-morphism $f:Y\to Z$ inducing $\phi$, subject to the following conditions.

Require $k_i\le k'_i$ for every $i$. For every $y\in Y$, $A'\in S'_y$ and $A\in S_{f(y)}$, require $$A'\phi(A)^{-1}\in P_k(\mathcal O_{Y,y}),$$ where $\phi$ acts entrywise. For every nonzero $g\in\mathcal O_{Z,f(y)}$ whose principal ideal is radical, the principal ideal generated by $\phi(g)$ in $\mathcal O_{Y,y}$ is radical.

For every field $K$, every point $x:\operatorname{Spec}K\to Z$, every $A\in S_{x_0}$ and every $h\in P_k(K)$, there is exactly one point $p:\operatorname{Spec}K\to Y$ such that $f\circ p=x$ and, for some $A'\in S'_{p_0}$, $$h\left(\bigl(A'\phi(A)^{-1}\bigr)(p)\right)^{-1}\in P_{k'}(K).$$ Here $x_0,p_0$ are the images of the unique point of $\operatorname{Spec}K$; evaluation at $p$ is entrywise through $\mathcal O_{Y,p_0}\to K$. A full-flag refinement has $k'=m$.

**Graded Cartier divisors.** Suppose $S'$ has type $m$. Write $\eta_Y$ for the generic point of $Y$ and $$\mathcal R_m=\{(i,a):i\in I,\ 0\le a<m_i\}.$$ A family of Cartier divisors $(D_{i,a})_{(i,a)\in\mathcal R_m}$ is graded for $S'$ if there is one $B\in S'_{\eta_Y}$ such that, for every $y\in Y$ and $(i,a)\in\mathcal R_m$, there is an $A\in S'_y$ for which $$t=(B_iA_i^{-1})_{aa}\ne0$$ is a local rational equation for $D_{i,a}$ at $y$: the germ of $D_{i,a}$ equals that of the principal Cartier divisor defined by $t$.

**Intersection polynomials.** Let $Y/F$ be smooth, geometrically integral and projective of dimension $d$, and let $(D_{i,a})$ be any Cartier divisors indexed by $\mathcal R_m$. Write $\deg_Y Q(D)$ for the real linear functional on $\mathbb R[x_{i,a}]$ which sends a degree-$d$ monomial $x_{r_1}\cdots x_{r_d}$ to the intersection degree $\deg(D_{r_1}\cdots D_{r_d})$ and sends every monomial of another total degree to zero.

For a polynomial $R\in\mathbb R[c_{i,j}:i\in I,\ j\in\mathbb N]$, let $R(e(x))$ be obtained by substituting the $j$th elementary symmetric polynomial in $x_{i,0},\ldots,x_{i,m_i-1}$ for $c_{i,j}$. The zeroth elementary symmetric polynomial is $1$, and those with $j>m_i$ are zero. Put $$P_m(x)=\prod_{i\in I}\prod_{a=0}^{m_i-1}(-x_{i,a})^{m_i-1-a},\qquad \Delta_m(x)=\prod_{i\in I}\prod_{0\le a<b<m_i}(x_{i,b}-x_{i,a}).$$ For $Q\in\mathbb R[x_{i,a}]$, define $$\operatorname{Alt}_m Q=\sum_{w\in\prod_{i\in I}\mathfrak S_{m_i}}\left(\prod_{i\in I}\operatorname{sgn}(w_i)\right)Q(x_{i,w_i(a)}).$$ Empty sums and products have their usual values $0$ and $1$.
