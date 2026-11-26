---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/IsKSValueOneOfRetraction.lean",
  "declarations": [
    "GlobalTheory.DeRham.AllPrim",
    "GlobalTheory.DeRham.Crys",
    "GlobalTheory.DeRham.Fil",
    "GlobalTheory.DeRham.GrpMor.Corr",
    "GlobalTheory.DeRham.GrpMor.IsBC",
    "GlobalTheory.DeRham.HdR",
    "GlobalTheory.DeRham.IsLieImage",
    "GlobalTheory.DeRham.IsPolForm",
    "GlobalTheory.DeRham.LieExact",
    "GlobalTheory.DeRham.PrimitiveSubmodule",
    "GlobalTheory.DeRham.crysToDR",
    "GlobalTheory.DeRham.liftFil",
    "GlobalTheory.DeRham.liftMor",
    "GlobalTheory.DeRham.prim",
    "GlobalTheory.DeRham.primDR",
    "GlobalTheory.DeRham.push",
    "GlobalTheory.DeRham.tanVal",
    "GlobalTheory.DeRham.wedgeForm"
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

## Divided-power cohomology and its primitive submodules

[Definition / hypothesis PHT.D021](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.IsNilDP/)

Work in a fixed universe of rings and schemes. Let $R$ be a commutative ring, let $I\subseteq R$ carry a divided-power structure $\gamma=(\gamma_n)_{n\ge0}$, and let $s:X\to\operatorname{Spec}R$ be a morphism of schemes.

**Nilpotence and thickenings.** A divided-power structure $\delta$ on an ideal $J\subseteq B$ is *nilpotent* if there is $N\in\mathbb N$ such that, for every finite list $a_1,\ldots,a_r\in J$ and $n_1,\ldots,n_r\in\mathbb N$ with $\sum_i n_i\ge N$, $$\prod_{i=1}^r\delta_{n_i}(a_i)=0.$$ The empty list is allowed, with empty sum $0$ and empty product $1$.

Define a category $\mathcal C_\gamma(X/R)$ as follows. An object $T$ consists of a commutative $R$-algebra $B_T$, an ideal $J_T\subseteq B_T$ with nilpotent divided powers $\delta_T$, a commutative ring $B_{T,0}$, a surjection $\pi_T:B_T\twoheadrightarrow B_{T,0}$ with kernel $J_T$, and a morphism $x_T:\operatorname{Spec}B_{T,0}\to X$. Require that the structure map $\alpha_T:R\to B_T$ respects divided powers: $$\alpha_T(I)\subseteq J_T,\qquad \alpha_T(\gamma_n(a))=\delta_{T,n}(\alpha_T(a))\quad(a\in I,\ n\in\mathbb N),$$ and that $s\circ x_T=\operatorname{Spec}(\pi_T\circ\alpha_T)$.

A morphism $f:T\to T'$ consists of an $R$-algebra homomorphism $f_*:B_T\to B_{T'}$ respecting the divided powers and a ring homomorphism $f_0:B_{T,0}\to B_{T',0}$ such that $$f_0\circ\pi_T=\pi_{T'}\circ f_*,\qquad x_{T'}=x_T\circ\operatorname{Spec}f_0.$$ Composition uses composition of these ring homomorphisms. The coefficient algebra at $T$ is $B_T$, and its map along $f$ is $f_*$.

**Cochains, cohomology and cup product.** A degree-zero cochain is a choice $a(T)\in B_T$ for every object. A degree-one cochain is a choice $c(f)\in B_{T_1}$ for every arrow $f:T_0\to T_1$. A degree-two cochain is a choice $z(f,g)\in B_{T_2}$ for every composable pair $T_0\xrightarrow{f}T_1\xrightarrow{g}T_2$. These choices form $R$-modules $C^0,C^1,C^2$, with pointwise operations. Define $$(d^0a)(f)=a(T_1)-f_*a(T_0),\qquad (d^1c)(f,g)=g_*c(f)-c(g\circ f)+c(g).$$ Let $Z^1$ consist of the cochains satisfying $d^1c=0$. Let $Z^2$ consist of the degree-two cochains satisfying $$h_*z(f,g)+z(g\circ f,h)=z(f,h\circ g)+z(g,h)$$ for every composable triple $T_0\xrightarrow{f}T_1\xrightarrow{g}T_2\xrightarrow{h}T_3$. Put $$H^1_\gamma(X/R)=Z^1/\operatorname{im}d^0,\qquad H^2_\gamma(X/R)=Z^2/\operatorname{im}d^1.$$ The cup product of degree-one classes is represented on cocycles by $$(c\smile c')(f,g)=g_*c(f)\,c'(g).$$

**Pullbacks.** Let $\sigma:R\to R'$ respect divided powers $\gamma$ on $I$ and $\gamma'$ on $I'$, and let $u:X'\to X$ satisfy $s\circ u=\operatorname{Spec}\sigma\circ s'$. An object of $\mathcal C_{\gamma'}(X'/R')$ gives an object of $\mathcal C_\gamma(X/R)$ by restricting its algebra structure along $\sigma$ and replacing $x_T$ by $u\circ x_T$. Precomposition of cochains along this functor defines $\sigma$-semilinear pullbacks $$u^*:H^q_\gamma(X/R)\longrightarrow H^q_{\gamma'}(X'/R')\qquad(q=1,2).$$

**The zero-ideal specialization and Hodge submodule.** Use the unique divided-power structure on the zero ideal of $R$, and write $$H^q_{\rm dR}(X/R)=H^q_0(X/R)\qquad(q=1,2).$$ Let $\mathcal C_{\rm triv}(X/R)$ be the full subcategory of $\mathcal C_0(X/R)$ on the objects with $J_T=0$. Apply the same cochain definitions on this subcategory. Restriction defines a map $\rho:H^1_{\rm dR}(X/R)\to H^1(\mathcal C_{\rm triv}(X/R),B)$, and put $$F^1(X/R)=\ker\rho.$$ Write $\mathscr F(X/R)$ for the $1$-cocycles on $\mathcal C_0(X/R)$ that vanish on every arrow between two objects with zero thickening ideal. Their class map is denoted $\operatorname{cl}:\mathscr F(X/R)\to H^1_{\rm dR}(X/R)$.

**Primitive classes and duals.** Let $S\to\operatorname{Spec}R$ be a morphism and let $A\to S$ be a group scheme, with multiplication $\mu:A\times_S A\to A$ and projections $p_1,p_2$. Its primitive submodule is $$P_\gamma(A/S)=\{c\in H^1_\gamma(A/R):\mu^*c=p_1^*c+p_2^*c\}.$$ Its primitive dual is $D_\gamma(A/S)=\operatorname{Hom}_R(P_\gamma(A/S),R)$. Saying that all degree-one classes are primitive means $P_\gamma(A/S)=H^1_\gamma(A/R)$.

For $A$ over $\operatorname{Spec}R$, put $$P_{\rm dR}(A)=P_0(A/\operatorname{Spec}R),\qquad D_{\rm dR}(A)=\operatorname{Hom}_R(P_{\rm dR}(A),R),$$ $$F^1_{\rm prim}(A)=\{c\in P_{\rm dR}(A):c\in F^1(A/R)\},\qquad \operatorname{Fil}(A)=\{\lambda\in D_{\rm dR}(A):\lambda(c)=0\text{ for all }c\in F^1_{\rm prim}(A)\}.$$

For a group homomorphism $A'\to A$ over a base change $S'\to S$ and $R\to R'$ respecting the divided powers, the induced primitive pullback is $\sigma$-semilinear. When $R'$ is viewed as an $R$-algebra via $\sigma$, its *base-change property* means that the linearized map $$R'\otimes_R P_\gamma(A/S)\longrightarrow P_{\gamma'}(A'/S'),\qquad b\otimes c\longmapsto b\,u^*c,$$ is bijective.

**Dual maps and correspondence under base change.** A group homomorphism $f:A\to B$ over the same base induces the $R$-linear map $$f_*:D_\gamma(A/S)\longrightarrow D_\gamma(B/S),\qquad (f_*d)(c)=d(f^*c).$$ For a group homomorphism $u:A'\to A$ over $S'\to S$ and a ring map $\sigma:R\to R'$ respecting divided powers, functionals $d\in D_\gamma(A/S)$ and $d'\in D_{\gamma'}(A'/S')$ *correspond under $u$* if $$d'(u^*c)=\sigma(d(c))\qquad(c\in P_\gamma(A/S)).$$

**Comparison for a lifted group scheme.** Let $\pi:R\twoheadrightarrow R_0$ have kernel $I$, with divided powers $\gamma$ on $I$. Let $A/R$ and $A_0/R_0$ be group schemes, and let $i:A_0\to A$ identify $A_0$ with $A\times_RR_0$ as a group scheme. Compute $P_\gamma(A_0)$ and $D_\gamma(A_0)$ over $R$, using the composite $A_0\to\operatorname{Spec}R_0\xrightarrow{\operatorname{Spec}\pi}\operatorname{Spec}R$. The map $i$ gives two primitive pullbacks: $$r_A:P_{\rm dR}(A)\longrightarrow P_{\rm dR}(A_0),\qquad c_A:P_{\rm dR}(A)\longrightarrow P_\gamma(A_0).$$ The reduction map $r_A$ uses zero divided powers over $R$ and $R_0$ and is $\pi$-semilinear. The comparison $c_A$ uses zero divided powers over $R$ in its domain and $\gamma$ over $R$ in its codomain, so is $R$-linear. Both are the pullbacks already defined by precomposition of cochains.

Define the dual comparison and lifted Hodge submodule by $$C_A:D_\gamma(A_0)\longrightarrow D_{\rm dR}(A),\qquad C_A(d)=d\circ c_A,$$ $$\operatorname{Fil}_\gamma(A/A_0)=C_A^{-1}(\operatorname{Fil}(A)).$$ Correspondence under reduction uses $r_A$ and the scalar map $\pi:R\to R_0$.

## Tangent evaluation and Chern pairings in divided-power cohomology

[Definition / hypothesis PHT.D022](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.SqExt.val/)

Use the categories, cochains, class map $\operatorname{cl}:\mathscr F(X/R)\to H^1_{\rm dR}(X/R)$, primitive submodules and primitive duals of ([Divided-power cohomology and its primitive submodules](https://andrewodesky.com/rh/lean/GlobalTheory.Cris.IsNilDP/)).

**Evaluation on tangent vectors.** Let $A$ be a group scheme over a commutative ring $R$, with identity $e:\operatorname{Spec}R\to A$. Write $R_\epsilon=R[\epsilon]/(\epsilon^2)$, let $\pi:R_\epsilon\to R$ send $\epsilon$ to $0$, and let $\iota:R\to R_\epsilon$ be the inclusion. A tangent vector at the identity is an $R$-morphism $v:\operatorname{Spec}R_\epsilon\to A$ satisfying $v\circ\operatorname{Spec}\pi=e$.

For such $v$, form three objects of $\mathcal C_0(A/R)$. Let $T_0$ be the trivial thickening at $e$, with coefficient and quotient ring $R$; let $T_1$ be the trivial thickening at $v$, with coefficient and quotient ring $R_\epsilon$. Let $T_v$ have coefficient ring $R_\epsilon$, ideal $(\epsilon)$, quotient map $\pi$ and reduced point $e$. Give $(\epsilon)$ the divided powers $\delta_0(a)=1$, $\delta_1(a)=a$ and $\delta_n(a)=0$ for $n\ge2$. There are arrows $$\alpha:T_0\to T_v,\qquad \beta:T_1\to T_v,$$ whose coefficient-ring maps are respectively $\iota$ and $\operatorname{id}_{R_\epsilon}$ and whose quotient-ring maps are respectively $\operatorname{id}_R$ and $\pi$.

For $f\in\mathscr F(A/R)$ define $$\langle v,f\rangle_\epsilon=[\epsilon]\bigl(f(\alpha)-f(\beta)\bigr)\in R,$$ where $[\epsilon](a+b\epsilon)=b$. A functional $\lambda\in D_{\rm dR}(A)$ and a tangent vector $v$ satisfy the *tangent-evaluation relation* if $$\lambda(\operatorname{cl}f)=\langle v,f\rangle_\epsilon$$ for every $f\in\mathscr F(A/R)$ whose class is primitive. The *Lie exactness condition* consists of both assertions: every $\lambda\in D_{\rm dR}(A)$ satisfies this relation with exactly one tangent vector, and every tangent vector satisfies it with at least one such functional.

**The divided-power Chern condition.** Let $I\subseteq R$ carry divided powers $\gamma$, let $X\to\operatorname{Spec}R$ be a morphism, and let $L$ be a line bundle on $X$ with a chosen presentation by an open cover $(U_i)_{i\in\mathcal I}$ and units $g_{ij}\in\Gamma(U_i\cap U_j,\mathcal O_X)^\times$. Use the convention $g_{ii}=1$ and $g_{ij}g_{jk}=g_{ik}$ on triple intersections, with local section coefficients satisfying $s_i=g_{ij}s_j$.

Let $\mathcal C_L$ be the full subcategory of $\mathcal C_\gamma(X/R)$ consisting of the objects $T$ whose reduced point $x_T:\operatorname{Spec}B_{T,0}\to X$ factors through some $U_i$. For $a\in J_T$, put $$\operatorname{Exp}_{\delta_T}(a)=\sum_{n\ge0}\delta_{T,n}(a).$$ This sum has finite support by the nilpotence condition on $\delta_T$.

A class $z\in H^2_\gamma(X/R)$ satisfies the *divided-power Chern condition for $L$* if there exist:

- a choice $i(T)\in\mathcal I$ for every $T\in\mathcal C_L$ such that $x_T$ factors through $U_{i(T)}$;
- an element $u(f)\in B_{T'}$ for every arrow $f:T\to T'$ of $\mathcal C_L$;
- a $2$-cocycle $\ell$ on $\mathcal C_L$ with its coefficient algebras $B_T$;

such that the following conditions hold. For every arrow $f:T\to T'$, $$\pi_{T'}(u(f))=x_{T'}^*g_{i(T'),i(T)}.$$ Here the right side is evaluation in $B_{T',0}$ on the overlap; the arrow ensures that $x_{T'}$ factors through both opens. For every composable pair $T\xrightarrow{f}T'\xrightarrow{g}T''$, require $$\ell(f,g)\in J_{T''},\qquad \operatorname{Exp}_{\delta_{T''}}(\ell(f,g))\,u(g\circ f)=g_*u(f)\,u(g).$$ Finally, the restriction of $z$ to $H^2(\mathcal C_L,B)$ is $[\ell]$.

**Chern pairings on the primitive dual.** Let $A\to S$ be a group scheme and let $S\to\operatorname{Spec}R$ be a morphism. For a line bundle $L$ on $A$, an $R$-bilinear form $\psi$ on $D_\gamma(A/S)$ is a *Chern pairing for $L$* if there exist $n\in\mathbb N$ and classes $a_k,b_k\in P_\gamma(A/S)$ for $0\le k<n$ such that $\sum_{k=0}^{n-1}a_k\smile b_k$ satisfies the divided-power Chern condition for $L$ and $$\psi(\lambda,\mu)=\sum_{k=0}^{n-1}\bigl(\lambda(a_k)\mu(b_k)-\lambda(b_k)\mu(a_k)\bigr)$$ for all $\lambda,\mu\in D_\gamma(A/S)$. Empty families, with zero sums, are allowed.
