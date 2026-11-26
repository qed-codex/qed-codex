---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/PointSeparationPair.lean",
  "declarations": [
    "GlobalTheory.Published.PointSeparationPair"
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

## Geometric and counting assumptions for the covolume bound

[Definition / hypothesis AG.D018](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.VolumeEstimateHypotheses/)

The following four groups of assumptions are used in ([The covolume bound from self-intersection, small-section and geometric estimates](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.topCovolG_alt_alt/)). In items 1 and 2, the twenty-eight statements in item (14) of ([Hypothesis list C: sixty assumed statements on resolution of singularities, arithmetic intersection theory, positivity of line bundles, toroidal compactifications, abelian schemes and p-divisible groups](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.ResolutionCharZero/)) are antecedents: the two implications are assumed, and item (14) is assumed separately in the theorem.

**Gram representations.** Let $K$ be a number field and $V$ a $K$-vector space. A family of functions $N_\sigma:V\to\mathbb R$, indexed by embeddings $\sigma:K\hookrightarrow\mathbb C$, has a Gram representation if there are $n\in\mathbb N$, a basis $b_0,\ldots,b_{n-1}$ of $V$, and matrices $A_v\in\mathrm{GL}_n(\mathbb C)$, one for each infinite place $v$ of $K$. Write $\sigma_v$ for its chosen representative embedding. For $x=\sum_i a_i b_i$, put $a^{\sigma_v}=(\sigma_v(a_i))_i$; then $$N_{\sigma_v}(x)=\left(\sum_{i=0}^{n-1}\left|(A_v^{-1}a^{\sigma_v})_i\right|^2\right)^{1/2}.$$ The dimension $n=0$ is allowed, with empty sum zero.

**1. A self-intersection estimate.** Suppose item (14) of that list holds. Let $K$ be a number field with no real embeddings, $V$ a $K$-vector space with compatible $\mathcal O_K$-module structure, $\Omega$ a field containing $K$, $W\subseteq V$ a finitely generated $\mathcal O_K$-module spanning $V$, and $\mathrm{ev}:V\to\Omega$ a $K$-linear map. Assume $\mathrm{ev}\ne0$ and that the ratios $\mathrm{ev}(v)/\mathrm{ev}(w)$ generate $\Omega$ over $K$. At each complex embedding of $K$ let a real-valued function on $V$ be given, equal at conjugate embeddings and admitting a Gram representation.

Let $D\in\mathbb N$, and let $\delta=\delta(\mathrm{ev},D)$ and $h=h(\mathcal N,W,\mathrm{ev},D)$ be the image degree and chosen image height in ([Image degrees and Chow heights of linear evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)), where $\mathcal N$ is the family of functions just specified. Assume $\delta>0$. Let $X$ be an integral scheme over $\mathcal O_K$ and $L$ a Hermitian line bundle with the chosen local weights of ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)). Choose a field map $\psi:\Omega\to K(X)$ and a map $s:W\to H^0(X,L)$. Require the arithmetic image-model condition of ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)) for $(\mathcal N,W,\mathrm{ev},D,X,L,\psi,s)$. If $a$ is an arithmetic self-intersection, in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)), of $L$ with its metric shifted by a real constant $t$, then $$a\le [K:\mathbb Q](D+1)\delta(h+t).$$

**2. A comparison of small-section counts.** Suppose item (14) of that list holds. Take any datum of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), any geometric core for this datum as in ([Adelic frames for unitary moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.Core/)), any stage $j\in\mathbb N$, and any cover satisfying the good-cover hypothesis of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)) for parameters $e\in\mathbb N$ and $o\in\mathbb R$. Let $E$ be the CM field and $K$ the cover's coefficient field. Require $$2<\left\lfloor\frac{[E:\mathbb Q]}2\right\rfloor.$$ For every irreducible component $Z$ after coefficient-field base change and every integral weight $u$, use the component cusp space $S_Z(u,0)$ and generic evaluation $\operatorname{ev}_Z:S_Z(u,0)\to\Omega_Z$ of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)). Put $$\Lambda_Z(u,0)=\Lambda(u,0)\cap S_Z(u,0).$$ Require the following conditions:

- The component norms on $S_Z(u,0)$, defined in ([Component Petersson norms, Bergman functions and small sections](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.muOn/)) at scale $x=|\phi_0(\xi_0)|$, admit a Gram representation. The integral submodule $\Lambda_Z(u,0)$ is finitely generated over $\mathcal O_K$ and spans $S_Z(u,0)$ over $K$.
- The evaluation map $\operatorname{ev}_Z$ is nonzero, and the ratios $\operatorname{ev}_Z(f)/\operatorname{ev}_Z(g)$, for $f,g\in S_Z(u,0)$, generate $\Omega_Z$ over $K$.
- For every nonzero prime $\lambda$ of $\mathcal O_K$, every ordinary evaluation valuation $v\in\mathcal R_\lambda$ of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)), every integer weight $(a,b)$ of ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)), and every $f\in\mathcal S_Z(a,b)$, require $$v(f)\ne+\infty\quad\Longrightarrow\quad\exists w\in\Lambda_Z(u,0),\qquad v(w)\ne+\infty.$$
- The component image degree $D_Z(u)$ in ([Image degrees and Chow heights of linear evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)) is positive.

Let $X$ be an integral scheme over $\mathcal O_K$, let $L$ be a Hermitian line bundle on $X$, and let $\Omega_Z$ embed into its function field. Choose a map $s:\Lambda_Z(u,0)\to H^0(X,L)$. Assume the arithmetic image-model condition of ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)) for this field map, $s$, the component norms, $\Lambda_Z(u,0)$ and $\operatorname{ev}_Z$, with the dimension of the stage's flag variety. For every integer $i\ge1$ and every real $t$, the extended cardinality of $\mathcal L_Z(u;8i,t)$ is at most that of the small sections of the $(8i)$th tensor power of $L$ after its metric is shifted by $t$. Here $\mathcal L_Z$ is defined in ([Component Petersson norms, Bergman functions and small sections](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.muOn/)), at the same scale $x=|\phi_0(\xi_0)|$. Metric shifts and small sections on $X$ have the definitions in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)).

**3. Five geometric and representation-theoretic statements.** Assume ([Seminegativity of a semiabelian Lie bundle](https://andrewodesky.com/rh/lean/GlobalTheory.Nef.semiAbelianLieSeminegative/)), the polynomial parametrization in ([Cuspidal characters of finite general linear groups](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)), and ([A point-separation hypothesis for klt pairs](https://andrewodesky.com/rh/s/def-klt-point-separation.html)). Assume also the following two assertions.

**Compactification with a logarithmic Kodaira–Spencer map.** For every choice of the moduli data in ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)) with $p+q\ge1$, and every invariant function $\phi$ satisfying the polarizing-fan and no-self-intersection conditions of ([Polarizing fan conventions for toroidal compactifications](https://andrewodesky.com/rh/lean/GlobalTheory.LocM.InvFun/)) over $\mathcal O_E$ in ranks at most $\min(p,q)$, there are a model $Y/K$, an effective Cartier divisor $B$ on $Y$, and integers $d,k\ge1$ such that $Y/K$ is smooth of relative dimension $[E:\mathbb Q]pq/2$, the reduced boundary $D$ has simple normal crossings, and $\operatorname{Supp}B$ is disjoint from the abelian locus. Every point of $D$ has a polarized boundary chart for $(\phi,B,d)$ in ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)). If the determinant Hodge presentation $\lambda$ is a line bundle, then $\lambda^{\otimes k}\otimes\mathcal O_Y(-B)$ is ample. The semiabelian extension, its polarization line, and the open subset $j(X)$ satisfy the logarithmic Kodaira–Spencer condition in ([Flag models and logarithmic Kodaira–Spencer maps](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)).

**Fubini–Study self-intersection.** Assume the following universally quantified assertion. Let $K$ be a number field, let $N,e,\delta\in\mathbb N$, and let $i:Y\hookrightarrow\mathbb P^N_{\mathcal O_K}$ be a closed immersion, with $Y$ integral, flat over $\mathbb Z$ and of absolute dimension $e+1$. Let $P_\eta\subseteq\mathcal O_K[X_0,\ldots,X_N]$ be the homogeneous prime corresponding to the point $i(\eta_Y)$, and set $I=P_\eta K[X_0,\ldots,X_N]$. For every family $A_\tau\in\mathrm{GL}_{N+1}(\mathbb C)$, indexed by all ring homomorphisms $\tau:\mathcal O_K\to\mathbb C$ and satisfying the conjugation condition in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)), and every Chow form $f$ of dimension $e$ and block degree $\delta$ for $I$ in ([Image degrees and Chow heights of linear evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)), put $$h_A(f)=\mathcal H_\delta(I_{N+1},A_K;f),\qquad (A_K)_\sigma=A_{\sigma|_{\mathcal O_K}}.$$ Here $I_{N+1}$ is the identity matrix, the polynomial has $e+1$ blocks of $N+1$ variables, and $\mathcal H_\delta$ is the normalized Chow height in ([Image degrees and Chow heights of linear evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.imageIdeal/)). Give $\mathcal O(1)$ the coordinate-section Fubini–Study metric of ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)). The assertion requires $$[K:\mathbb Q]h_A(f)$$ to be an arithmetic self-intersection of $i^*\overline{\mathcal O(1)}$, with the meaning in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)).

**4. Further geometric statements.** Assume the Hilbert–Samuel inputs in ([Global hypotheses for cusp ratios](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.Hypotheses''/)), ([Integral Siegel compactifications with quadratic period charts](https://andrewodesky.com/rh/s/def-integral-siegel-compactifications.html)), items (13a) and (13b) of the titled hypothesis list C, and the following two statements.

- For every choice of moduli data and fan in the compactification assertion of item 3, there are $Y,B,d,k$ with all its model, smoothness, simple normal-crossing boundary, support, polarized-chart and conditional ampleness properties.
- For every choice of the moduli data in ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)) with $p+q\ge1$, there is a model $Y/K$, smooth of relative dimension $[E:\mathbb Q]pq/2$, whose reduced boundary has simple normal crossings and whose every boundary point has an ordinary boundary chart in ([Unitary toroidal models and boundary charts](https://andrewodesky.com/rh/lean/GlobalTheory.MumfordChart.HasChart/)).

## Hypothesis list C: sixty assumed statements on resolution of singularities, arithmetic intersection theory, positivity of line bundles, toroidal compactifications, abelian schemes and p-divisible groups

[Definition / hypothesis ARAK.D046](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.ResolutionCharZero/)

Assume the following fifteen hypotheses for ([The covolume bound, given hypothesis list C](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt/)).

**Arithmetic varieties in coordinates.** Items (3), (4) and (8) use the following description. Fix a finite set $K$ and finite sets $\iota_k$ for $k\in K$, and let $S=\mathbb{Z}[x_{k,i}:k\in K,\ i\in\iota_k]$ with its grading by $\mathbb{N}^K$.

- An *arithmetic variety of dimension $d$ in coordinates* is a multihomogeneous prime ideal $P$ of $S$, with $K$ nonempty, such that every block contains a variable $x_{k,i}\notin P$, $P\cap\mathbb{Z}=0$, and $\dim S/P=d+|K|$. It is the ideal of an integral closed subscheme $X_P$ of the product of projective spaces $\prod_k\mathbb{P}^{|\iota_k|-1}_{\mathbb{Z}}$ that dominates $\operatorname{Spec}\mathbb{Z}$; the last condition says that $X_P$ has dimension $d$. We write $X_P(\mathbb{C})$ for the set of $z\in\prod_k\mathbb{C}^{\iota_k}$ with every block $z_k$ nonzero at which all elements of $P$ vanish.
- When a field $\Omega$ and elements $y_{k,i}\in\Omega$ are given, $P_y$ is the kernel of $S\to\Omega[T_k:k\in K]$, $x_{k,i}\mapsto y_{k,i}T_k$. The $y_{k,i}$ are *birational coordinates* if every element of $\Omega$ is a quotient $g(y)/h(y)$ of multihomogeneous polynomials of the same degree; then $\Omega$ is the function field of $X_{P_y}$.
- A *metrised line bundle* $A=(a,h_A)$ consists of $a\in\mathbb{Z}^K$ and a positive function $h_A$ on the set of $z$ with every block nonzero such that $h_A(cz)=\prod_k|c_k|^{a_k}h_A(z)$ for $c\in(\mathbb{C}^\times)^K$. It stands for the line bundle $\mathcal{O}(a)$ with the metric $\|s\|(z)=|s(z)|/h_A(z)$ on multihomogeneous polynomials $s$ of degree $a$. It is *smooth* if $h_A$ is $C^\infty$, and *invariant under conjugation* if $h_A(\bar z)=h_A(z)$. A *section* of $A$ on $X_P$ is a multihomogeneous $s\in S$ of degree $a$ with $s\notin P$.
- The sections of $\tau A$ in $\Omega$, for birational coordinates $y$ and $\tau\ge0$, form the group $\Gamma_\tau(A)$ of all $s\in\Omega$ such that $s\prod_k y_{k,c_k}^{-\tau a_k}$ lies in the ring $\mathbb{Z}[y_{k,i}/y_{k,c_k}]$ for every choice of indices $c_k\in\iota_k$ with all $y_{k,c_k}\ne0$; $\Gamma^{\nu}_\tau(A)$ is defined in the same way with the integral closures of these rings in $\Omega$. An element $s$ is *small* if $|g(z)|\le|h(z)|\,h_A(z)^{\tau}$ for every $z\in X_{P_y}(\mathbb{C})$ and every pair of multihomogeneous polynomials $g,h$ with $g(y)=s h(y)$ and $\deg g=\deg h+\tau a$. Put $\hat h^0(\tau A)=\log\operatorname{card}_0\{s\in\Gamma_\tau(A)\ \text{small}\}$, and $\hat h^0_\nu(\tau A)$ likewise with $\Gamma^\nu_\tau(A)$. Here $\operatorname{card}_0$ is cardinality for finite sets and zero for infinite sets, $\log 0=0$, and division by zero in the displayed sequences is zero.
- An *intersection pairing* is a rule that assigns a real number $(\hat L_1\cdots\hat L_n\cdot X_P)$ to every $K$, $(\iota_k)$, ideal $P$ and metrised line bundles $L_1,\dots,L_n$, with three properties for arithmetic varieties $P$ of dimension $n$ and smooth $L_j$: it is symmetric in the $L_j$; it is additive in each $L_j$ under tensor product; and for every section $s$ of $L_n$, $$(\hat L_1\cdots\hat L_n\cdot X_P)=\sum_{W}m_W\,c_W-I(P,s;L_1,\dots,L_n),$$ where $W$ runs over the components of the divisor of $s$ on $X_P$ with multiplicities $m_W$, $c_W=(\hat L_1\cdots\hat L_{n-1}\cdot X_W)$ if $W\cap\mathbb{Z}=0$ and $c_W=(L_1\cdots L_{n-1}\cdot X_W)\log p$ if $W$ contains the prime $p$, and $I$ is an integral over $X_P(\mathbb{C})$ (components, multiplicities, the geometric intersection number and the integral were not expanded). This is the inductive definition of arithmetic intersection numbers.
- $A$ is *semipositive relative to $P_0\subseteq P$* if it is smooth and the Levi form of $\log h_A$ is nonnegative at every point of $X_P(\mathbb{C})$ on the vectors tangent to the cone of $P_0$ (tangency not expanded). It is *nef on the fibres* of $X_P$ if $\mathcal{O}(a)$ has nonnegative degree on every one-dimensional $X_W$ with $W\supseteq P$ multihomogeneous prime of positive characteristic, and *nef on the generic fibre* if a degree (an integral over $X_W(\mathbb{C})$, not expanded) is nonnegative for every arithmetic variety $W\supseteq P$ of dimension 2.

**Arithmetic varieties as schemes.** Item (13) uses schemes. Let $k$ be an integral domain that is finitely generated as a $\mathbb{Z}$-module. An *arithmetic variety of relative dimension $D$ over $k$* is an integral scheme $X$ with a closed immersion into some $\mathbb{P}^N_k$, flat over $\mathbb{Z}$, of Krull dimension $D+1$. A *Hermitian line bundle* $\hat L$ on $X$ is a line bundle with, for every ring homomorphism $\sigma\colon k\to\mathbb{C}$, a smooth metric datum on the complex points for $\sigma$, compatible with complex conjugation (the metric datum was not expanded). A *height function* for $\hat L$ is a real function $h$ on the points of $X$ such that, for integral closed subschemes $Z$ with generic point $\eta_Z$: if $Z$ is a scheme of dimension $d$ over a finite field $\kappa$ then $h(\eta_Z)=(L|_Z)^d\log\#\kappa$; if $Z$ has characteristic $0$ and dimension 1 then $h(\eta_Z)$ is the arithmetic degree of $\hat L|_Z$; and if $Z$ has characteristic $0$ and dimension $e+1\ge2$ then for every $m$ and every rational section $r$ of $L^m|_Z$, $m\,h(\eta_Z)=\sum_z\operatorname{mult}_z(\operatorname{div}r)\,h(z)$ minus an archimedean integral (not expanded). We write $\hat L^{D+1}=a$ if some height function for $\hat L$ takes the value $a$ at the generic point of $X$. A section of $L$ is *small* if its norm is at most 1 at every complex point for every $\sigma$. $\hat L$ is *nef* if its metrics are semipositive (not expanded), $L$ has nonnegative degree on every vertical curve, and $\hat L$ has nonnegative arithmetic degree on every integral closed subscheme of characteristic $0$ and dimension 1.

**The statements.**

**(1)** Assume ([Resolution in characteristic zero](https://andrewodesky.com/rh/lean/PositivityTheory.Resplug.ResolutionBlowup.resolutionCharZero/)).

**(2)** *Principalisation of an ideal sheaf in characteristic 0.* Let $X$ be smooth of relative dimension $d$, quasi-compact and separated over a field $k$ of characteristic $0$, let $I$ be an ideal sheaf whose support contains no irreducible component of $X$, and let $E$ be a closed subset with simple normal crossings at each of its points. There are $s\colon X'\to X$ and a closed subset $E'$ of $X'$, obtained by a sequence of blow-ups of a restricted kind relative to $E$ (read in part), such that $X'$ is smooth over $k$, the pulled-back ideal $I\mathcal{O}_{X'}$ is locally generated by one non-zero-divisor, its support has simple normal crossings, and $s$ is an isomorphism over the complement of the support of $I$.

**(3)** *A Poincaré-Lelong identity.* Let $P$ be an arithmetic variety of dimension $n+2$ in coordinates, let $L_1,\dots,L_n,A,B$ be smooth metrised line bundles invariant under conjugation, with $B$ of degree $0$, and let $s$ be a section of $A$. The project attaches to $e$ real functions $\varphi_1,\dots,\varphi_e$ and a real function $g$ a number $J_P(\varphi;g)$, defined through a linear projection of $X_P(\mathbb{C})$ (not expanded). The statement is $$J_P\bigl(\log h_B,\log h_{L_1},\dots,\log h_{L_n};\ \log\|s\|\bigr)=\sum_{W}m_W\,J_W\bigl(\log h_{L_1},\dots;\ \log h_B\bigr)-J_P\bigl(\log h_A,\log h_{L_1},\dots;\ \log h_B\bigr),$$ the sum over the components $W$ of the divisor of $s$ with $W\cap\mathbb{Z}=0$. If $J_P(\varphi;g)=\int_{X_P(\mathbb{C})}g\,dd^c\varphi_1\wedge\dots\wedge dd^c\varphi_e$, this is Stokes' theorem combined with the Poincaré-Lelong formula $dd^c\log\|s\|^{-1}=c_1(A)-\delta_{\operatorname{div}s}$, up to the normalisation of $dd^c$.

**(4)** Assume all three assertions of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(4a)** Assume assertion 1 of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(4b)** Assume assertion 2 of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(4c)** Assume assertion 3 of ([Three arithmetic intersection and small-section hypotheses](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)).

**(5)** Assume ([Arithmetic intersection and volume](https://andrewodesky.com/rh/lean/PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright/)).

**(6)** Assume the orthogonality assertion (2) of ([Hodge–Tate maps, orthogonality and a cokernel bound](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate/)).

**(7)** Assume ([A polarized retract hypothesis over valuation rings](https://andrewodesky.com/rh/s/def-polarized-retract-valuation-ring.html)).

**(8)** Assume ([A nef section-dimension asymptotic in homogeneous coordinates](https://andrewodesky.com/rh/s/def-nef-normalized-section-asymptotic.html)).

**(9)** Assume ([Integral Siegel compactifications with quadratic period charts](https://andrewodesky.com/rh/s/def-integral-siegel-compactifications.html)).

**(10)** Assume the assertion “Compactification with a logarithmic Kodaira–Spencer map” in item 3 of ([Geometric and counting assumptions for the covolume bound](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.VolumeEstimateHypotheses/)).

**(11)** Assume ([Seminegativity of a semiabelian Lie bundle](https://andrewodesky.com/rh/lean/GlobalTheory.Nef.semiAbelianLieSeminegative/)).

**(12)** Assume ([A point-separation hypothesis for klt pairs](https://andrewodesky.com/rh/s/def-klt-point-separation.html)).

**(13)** Assume both statements below.

**(13a)** *Birational invariance of arithmetic self-intersection.* Let $R$ be a commutative domain finite as a $\mathbb Z$-module, and let $D\in\mathbb N$. Let $X$ and $X'$ be integral schemes with projective structure maps $p:X\to\operatorname{Spec}R$ and $p':X'\to\operatorname{Spec}R$. Require both schemes to be flat over $\mathbb Z$ and to have absolute dimension $D+1$. For every ring homomorphism $\sigma:R\to\mathbb C$, require that both $X_\sigma(\mathbb C)$ and $X'_\sigma(\mathbb C)$ are covered by the $D$-dimensional algebraic coordinate charts in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)).

Let $\pi:X'\to X$ be any morphism over $R$ such that, for some nonempty open $U\subseteq X$, the restriction $\pi^{-1}(U)\to U$ is an isomorphism. For every Hermitian line bundle $\overline L$ on $X$ and every $a\in\mathbb R$, if $a$ is an arithmetic self-intersection of $\overline L$, then it is an arithmetic self-intersection of $\pi^*\overline L$. Use the metric, height and self-intersection conventions of ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)); the pulled-back metric is obtained by composing each local potential with $\pi$ on complex points.

**(13b)** *The top power of the first Chern form integrates to the degree.* Let $F$ be a field, let $Y/F$ be a smooth geometrically integral projective variety of dimension $d\in\mathbb N$, with a chosen closed immersion into some $\mathbb P_F^N$, and let $\sigma:F\hookrightarrow\mathbb C$ be an embedding. Let $\Delta$ be a Cartier divisor on $Y$, let $L$ be a line bundle, and choose a nonzero rational section $r$ of $L$ with Cartier divisor $\Delta$.

Choose a smooth metric $\phi$ on $L$ at $\sigma$, using the local-potential transition and smoothness conditions in ([Arithmetic image models and Hermitian metrics](https://andrewodesky.com/rh/lean/GlobalTheory.ImageModel.IsModelOf/)) at this embedding. Let $\mu^+_{\phi,\sigma,d}$, $\mu^-_{\phi,\sigma,d}$ and $\mathcal I_{\phi,\sigma,d}$ be the signed Chern measures and integral in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)), applied to these local potentials. The constant function $1$ is integrable over all of $Y_\sigma(\mathbb C)$ against each of these two measures, and $$\mathcal I_{\phi,\sigma,d}\bigl(Y_\sigma(\mathbb C),1\bigr)=\deg_F(L^d).$$ Here the geometric top intersection on the right has the Euler-characteristic definition in ([Arithmetic heights and self-intersections of Hermitian line bundles](https://andrewodesky.com/rh/lean/GlobalTheory.HermLB.IsArithHeight/)); it is the $d$-fold self-intersection of $\Delta$.

**(14)** Assume all twenty-eight assertions of ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)). The labels below refer to the assertions of ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)) in their numbered order.

**(14.1)** Assertion 1: Unitary compactification.

**(14.2)** Assertion 2: Lower bound for arithmetic volume.

**(14.3)** Assertion 3: Volume of a nef bundle.

**(14.4)** Assertion 4: Arithmetic intersection laws.

**(14.5)** Assertion 5: Abelian de Rham assertions.

**(14.6)** Assertion 6: Ray class fields.

**(14.7)** Assertion 7: Potential semiabelian reduction.

**(14.8)** Assertion 8: Strong approximation.

**(14.9)** Assertion 9: Finite-field character series.

**(14.10)** Assertion 10: Good metrics and flag intersections.

**(14.11)** Assertion 11: Hermitian isometries.

**(14.12)** Assertion 12: Quadratic norm equations.

**(14.13)** Assertion 13: Extension of homomorphisms.

**(14.14)** Assertion 14: Simplicity in the closed lowest alcove.

**(14.15)** Assertion 15: A principal polarization has one section.

**(14.16)** Assertion 16: Torsion points.

**(14.17)** Assertion 17: Deformations over divided-power thickenings.

**(14.18)** Assertion 18: Prismatic and Hodge comparison.

**(14.19)** Assertion 19: Kawamata–Viehweg vanishing.

**(14.20)** Assertion 20: Nef numerical assertions.

**(14.21)** Assertion 21: Logarithmic $L^2$ extension.

**(14.22)** Assertion 22: Arithmetic Hilbert–Samuel.

**(14.23)** Assertion 23: Chow forms.

**(14.24)** Assertion 24: Cycle heights.

**(14.25)** Assertion 25: Algebraization of holomorphic sections.

**(14.26)** Assertion 26: Vanishing and isolated non-klt divisors.

**(14.27)** Assertion 27: Principalization.

**(14.28)** Assertion 28: Formal algebraization.

**(15)** *Deformations along divided-power thickenings.* For every commutative ring $R$, every ideal $I$ with nilpotent divided powers, and every surjection $R\to R_0$ with kernel $I$, assume the three deformation assertions of (14.17).

## A point-separation hypothesis for klt pairs

[Definition / hypothesis AG.D049](https://andrewodesky.com/rh/s/def-klt-point-separation.html)

Require the following assertion for every integral normal locally Noetherian projective scheme $X/\mathbb C$ of dimension $n\ge0$.

Let $\Delta$ be an effective rational Weil divisor on $X$, let $m,r$ be positive integers, and let $G$ be a Cartier divisor representing $m(K_X+\Delta)$ in the convention below. Assume $(X,\Delta)$ is klt at every point. Let $M$ and $N$ be line bundles, with $N$ nef and big, and suppose that for every complete integral curve $C\subseteq X$, $$M\cdot C=\frac{G\cdot C}{m}+\frac{N\cdot C}{r}.$$

Let $x_1\ne x_2$ be closed points of $X$ and let $c:\mathbb N\to\mathbb R$ satisfy $c(e)>0$ for $1\le e\le n$. For every irreducible closed subvariety $Z\subseteq X$ containing at least one of $x_1,x_2$ and of dimension $e\ge1$, require $$c(e)^e<\frac{N^e\cdot Z}{r^e}.$$ Suppose also that $$\sum_{e=1}^n\frac{2^{1/e}e}{c(e)}\le1.$$ Then there exists a global section $s\in H^0(X,M)$ vanishing at exactly one of $x_1,x_2$.
