---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/RhoGeo.lean",
  "declarations": [
    "Formalism.IndefR.FWT.RhoGeo"
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

## One-map and geometric comparison laws

[Definition / hypothesis ARAK.D223](https://andrewodesky.com/rh/lean/Formalism.IndefR.FWT.FWTie/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)) and ([Scalar normalizations and adelic period identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsJ/)). Write $K$ for the coefficient field, $K_s$ for the coefficient field of the original moduli, $\jmath:K\hookrightarrow\mathbb C$ for the distinguished embedding, and $\sigma_s=\sigma|_{K_s}$. An allowed $\sigma_s$ is an embedding preserving the specified complex square root. At stage $j+1$, let $C_j$ be the $K_s$-space of algebraic cusp forms of the chosen nonnegative weight and scalar degree, $W_j^{K_s}\subseteq K^{n_j}$ its analytic rational form, $H_{j,\sigma}$ its complex Hilbert realization, and $J_{j,\sigma}:K^{n_j}\to H_{j,\sigma}$ its specified semilinear map. Let $\Phi_{j,\sigma_s}(f)$ be the algebraic form's adelic function, including its prescribed Lie factor and domain scalars.

Hypothesis (algebraic and analytic comparison). The map $K_s\to K$ on algebraic integers is the prescribed coefficient-ring map. There is a $K_s$-linear isomorphism $e_j:C_j\simeq W_j^{K_s}$ for every $j$. The space $W_j^{K_s}$ has a finite $K_s$-basis that is also a $K$-basis of $K^{n_j}$. The positive and negative highest-weight entries of the algebraic weight equal the prescribed coefficient-representation weights, and its scalar degree is $n_V$.

For every finite prime $\lambda$ of $K_s$ there is a bijection between the analytic norm-test points and the moduli norm-test points. Under this bijection their seminorms agree on $e_jf$ and $f$. The original moduli choices satisfy ([Scalar normalizations and adelic period identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsJ/)).

At each allowed $\sigma_s$, the prescribed unitary Hecke character $\chi_{j,\sigma_s}$ is trivial on the embedded $F$-ideles and has infinite exponent $-e_{j,\sigma,\tau}$ at every infinite factor $\tau$, where $e_{j,\sigma,\tau}$ is the prescribed character weight transported through $\sigma$. For every idele $x$ with trivial infinite component there exists $a\in K_s$ such that $$\mu_{0,j+1}(x)=\jmath(a),\qquad \chi_{j,\sigma_s}(x)=\sigma_s(a).$$ If $\sigma_s$ is the distinguished embedding, require $\chi_{j,\sigma_s}=\mu_{0,j+1}$.

Choose, for every $j,\sigma$, a tuple $v_{j,\sigma}$ of unit lowest-type vectors of the discrete-series model. Each is an extremal weight vector: on a diagonal compact torus with angles $(\alpha_a)$ it transforms by $\exp(\mathrm i\sum_a\mu_a\alpha_a)$, for the model's fixed lowest compact weight in its prescribed reversed-negative order. At the distinguished embedding impose this additional conditional normalization: if any such extremal tuple pairs with a unit coefficient vector to $\Delta_j$, the chosen tuple does too. Thus there are lowest-type vectors representing the chosen tuple and a unit coefficient vector $w$ with $B_j(\bigotimes v,w)=\Delta_j$ whenever that normalization is realizable.

At every allowed $\sigma_s$, the fixed moduli base frame equals the model's orthonormal frame, with its columns put in the prescribed positive/negative order. Impose the following conditional comparison. If there exists a $\sigma$-semilinear map $L:K^{n_j}\to H_{j,\sigma}$ satisfying $$\operatorname{ev}_{v_{j,\sigma}}(L(e_j f))=\Phi_{j,\sigma_s}(f)\quad(f\in C_j),$$ then the specified map $J_{j,\sigma}$ satisfies the same equation. If there is no such $L$, require $J_{j,\sigma}=0$. Every equality here is required for every identification of the moduli Hermitian space with $W_j$ of the indicated type.

At a disallowed $\sigma_s$, use instead the complex conjugate of the algebraic adelic function at the conjugate coefficient embedding. If some unit tuple $v$ and some $\sigma_s$-semilinear map from $C_j$ into $H_{j,\sigma}$ evaluate to that conjugate function, then there is a unit tuple $v$ such that the map induced by $J_{j,\sigma}e_j$ evaluates to it. If no such unit tuple and semilinear map exist, require $J_{j,\sigma}=0$.

Hypothesis (geometric finite-group action). Let $O_j$ be the one-step coefficient realization in ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)) and let $A_j(g)$ be the induced operator on algebraic scalar rules. If all $A_j(g)$ preserve $C_j$, require $$e_j(A_j(g)f)=\rho_j(g)e_j(f)\quad(g\in G,\ f\in C_j).$$ If this preservation fails, every $\rho_j(g)$ is the identity. The implication has one antecedent asserting preservation for all $g$.

For allowed $\sigma_s$ and any chosen domain scalars $c$, define the equivariance condition as follows. For every $g\in G$, every finite-level lift $k_g$ of its specified residue matrix, and every $f\in C_j$, the form $A_j(g)f$ lies in $C_j$ and there is $a\in K_s$ with $$\jmath(a)=\prod_{P\in P_g}\chi_{j+1,P}(\det e_G(g)_P),\qquad \Phi_{j,\sigma_s,c}(A_j(g)f)(h)=\sigma_s(a)\Phi_{j,\sigma_s,c}(f)(hk_g)\quad(h\in G_j(\mathbb A_F)).$$ If some domain scalars of modulus one satisfy this condition, the fixed domain scalars $c_{j,\sigma_s}$ satisfy it.

Use the one-map comparison defined in ([Geometric theta class evaluations](https://andrewodesky.com/rh/lean/Formalism.IndefR.FWT.OMPins/)). If the distinguished one-step coefficient realization admits some domain scalars and phase satisfying that comparison, then it admits the fixed domain scalars with some phase. Under the same antecedent it satisfies the comparison with both the fixed domain scalars and the specified phase $\mathrm{ph}_j$.
