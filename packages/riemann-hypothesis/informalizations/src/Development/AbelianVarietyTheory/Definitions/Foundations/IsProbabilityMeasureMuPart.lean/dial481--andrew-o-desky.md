---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Foundations/IsProbabilityMeasureMuPart.lean",
  "declarations": [
    "GlobalTheory.AllWt.Weight",
    "GlobalTheory.AllWt.bergOn",
    "GlobalTheory.AllWt.cuspOn",
    "GlobalTheory.AllWt.cuspW",
    "GlobalTheory.AllWt.homN",
    "GlobalTheory.AllWt.latW",
    "GlobalTheory.AllWt.lieFacZ",
    "GlobalTheory.AllWt.muOn",
    "GlobalTheory.AllWt.petOn",
    "GlobalTheory.AllWt.wtOf"
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

## Component Petersson norms, Bergman functions and small sections

[Definition / hypothesis ARAK.D012](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.muOn/)

Use a good level cover, its coefficient field $K$, CM field $E$, signature $(p,q)$, irreducible component $Z$, cusp spaces $S_Z(v,0)$ and integral submodules $\Lambda_Z(v,0)$ from ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)). Let $v\in\mathbb Z^{\Psi\times\{0,\ldots,p+q-1\}}$ be an integral weight and let $x\in\mathbb R$ be the scale in ([Homogeneous norms on unitary frame domains](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.homN/)).

**Conditioning on a component.** Fix a permitted embedding $\sigma:K\hookrightarrow\mathbb C$, meaning $\sigma(\rho_\infty)=\rho_\infty$. Let $W$ be the chosen Hermitian space at this embedding, with reference lattice and recorded signatures, and put $$G=U(W)(\mathbb A_F),\qquad Q=U(W)(F)\backslash G.$$ Use the chosen quotient measure $\nu_W$ constructed in the conventions of ([Original moduli uniformizations and cusp norms](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM/)), including the alternatives for signature arrays and the arbitrary measure-and-set choice when no compatible fundamental-domain pair exists. Define $$\nu_W^1=\begin{cases} \nu_W(Q)^{-1}\nu_W,&0<\nu_W(Q)<+\infty,\\ \delta_{[1]},&\nu_W(Q)=0\text{ or }+\infty, \end{cases}$$ where $[1]\in Q$ is the identity coset and $\delta_{[1]}$ is its Dirac measure. Fix one representative $s(q)\in G$ of every $q\in Q$.

Write $\delta:G\to\coprod_c\{\text{ambient frames for }\mathcal D_c\}$ for the frame dictionary of ([Adelic frames for unitary moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.Core/)), and $u_c$ for the uniformization map on $\mathcal D_c$. Set $$A_{Z,\sigma}=\{q\in Q:\delta(s(q))=(c,z),\ z\in\mathcal D_c,\ \text{the point underlying }u_c(z)\text{ lies in }Z\}.$$ The measure used on the component is $$\mu_{Z,\sigma}=\nu_W^1(A_{Z,\sigma})^{-1}\bigl(\nu_W^1|_{A_{Z,\sigma}}\bigr).$$ In particular this formula gives the zero measure when $\nu_W^1(A_{Z,\sigma})=0$.

**Petersson norms and Bergman functions.** Let $\nu^\sigma(v)$ be the induced domain weight. For a family $P=(P_c)_c$ of complex functions on the ambient frame spaces, write $p_{\sigma,v}(P,(c,z))$ for its invariant pointwise norm with that weight, as defined in ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)). Put $$\mathcal H_{\sigma,v}=\operatorname{span}_{\mathbb C}\{P:P_c\text{ is a holomorphic cusp function of weight }\nu^\sigma(v)\text{ for every }c\}.$$ Here holomorphic cusp means the transformation, bounded invariant norm and vanishing constant Fourier–Jacobi coefficient conditions of ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)). For every family $P$, define the extended nonnegative quantity $$R_{Z,\sigma,v}(P)=\left(\int_Q p_{\sigma,v}(P,\delta(s(q)))^2\,d\mu_{Z,\sigma}(q)\right)^{1/2}\in[0,+\infty].$$ The integral is the nonnegative integral, allowing infinity. For a domain frame $y=(c,z)$, define $$B_{Z,\sigma,v}(y)=\sup_{P\in\mathcal H_{\sigma,v}} \frac{p_{\sigma,v}(P,y)^2}{R_{Z,\sigma,v}(P)^2}\in[0,+\infty].$$ The supremum ranges over the entire analytic space $\mathcal H_{\sigma,v}$; the component enters through $\mu_{Z,\sigma}$.

For an algebraic cusp rule $f\in S_Z(v,0)$, let $N_{x,\sigma,v}(f,y)$ be the homogeneous pointwise norm of its analytic reading, extended by zero outside the domains, as defined in ([Homogeneous norms on unitary frame domains](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.homN/)). Its real component Petersson norm is $$\|f\|_{Z,\sigma,v}=\operatorname{real}\left(\left(\int_Q N_{x,\sigma,v}(f,\delta(s(q)))^2\,d\mu_{Z,\sigma}(q)\right)^{1/2}\right),$$ where $\operatorname{real}(a)=a$ for finite $a\ge0$ and $\operatorname{real}(+\infty)=0$. For an arbitrary embedding $\sigma:K\hookrightarrow\mathbb C$, use $\sigma$ itself when it is permitted and use $\bar\sigma$ otherwise; the dictionary, domains and conditional measure in this formula are taken at that chosen permitted embedding.

**Small sections.** For every nonzero prime $\lambda\subset\mathcal O_K$ and every ordinary evaluation valuation $w\in\mathcal R_\lambda$ of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)), put $$d_{Z,v}(w)=\inf_{a\in\Lambda_Z(v,0)}w(a)\in[-\infty,+\infty].$$ For $h\in\mathbb N$ with $h\ge1$ and $t\in\mathbb R$, define $\mathcal L_Z(v;h,t)$ to be the set of $f\in S_Z(hv,0)$ satisfying both conditions:

- For every such $\lambda$ and $w$, one has $h\,d_{Z,v}(w)\le w(f)$.
- For every permitted $\sigma$ and every domain frame $y=(c,z)$ whose underlying point $u_c(z)$ lies in $Z$, one has $$N_{x,\sigma,hv}(f,y)^2\le \exp(2ht)\,B_{Z,\sigma,v}(y)^h.$$

The second inequality is in the extended nonnegative reals. The cardinality of this set is its finite cardinality when finite and $+\infty$ otherwise.

## Homogeneous norms on unitary frame domains

[Definition / hypothesis ARAK.D045](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.homN/)

Use the CM field $E$, coefficient field $K$, CM type $\Psi$, signature $(p,q)$ and uniformizing domains of ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)), writing $p=p_{\rm sig}$, $q=q_{\rm sig}$ and $N=p+q$. Let $\rho_\infty\in\mathbb C$ be the square root of $-d_{\rm mod}$ fixed in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)); it lies in $K$.

Let $v\in\mathbb Z^{\Psi\times\{0,\ldots,N-1\}}$. Fix an embedding $\sigma:K\hookrightarrow\mathbb C$ with $\sigma(\rho_\infty)=\rho_\infty$, a domain label $c$, a function $F_c:\mathcal D_c\to\mathbb C$ and a point $z\in\mathcal D_c$. Let $\nu^\sigma(v)$ and $P_{\sigma,c,v}(F_c,z)$ denote the induced domain weight and the invariant pointwise norm with that weight, using the definitions in ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)).

Define $$H(v)=\sum_{\tau\in\Psi}\left(\sum_{i=0}^{p-1}v_{\tau,i}-\sum_{i=0}^{q-1}v_{\tau,N-1-i}\right).$$ For any $x\in\mathbb R$, the homogeneous norm is $$N_{x,\sigma,c,v}(F_c,z)= \exp\left(-\frac{H(v)}2\log(2\pi x)\right)P_{\sigma,c,v}(F_c,z).$$ For an algebraic section of weight $(v,0)$, take $F_c$ to be its analytic reading on that domain. In degree $h\in\mathbb N$, use weight $hv$ in this definition.

## Cusp spaces and integral lattices on level covers

[Definition / hypothesis AV.D238](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)

These conventions define the cusp spaces, their generic evaluations and their integral submodules used in the weight statements. The arithmetic datum is one member satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with all of the conditions cited there. The comparison-law and good-cover hypotheses are distinguished below.
