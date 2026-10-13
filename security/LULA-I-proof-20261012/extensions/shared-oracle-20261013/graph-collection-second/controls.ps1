$ErrorActionPreference = 'Stop'
# COMPUTED controls: source-shaped integer counts and finite predicate checks only.
# No source cryptography, signatures, attack, graph/cache construction or benchmark.
function Check([bool]$condition,[string]$label) {
    if (-not $condition) { throw $label }
    $script:passed.Add($label)
}
$passed = [System.Collections.Generic.List[string]]::new()
$hs=@(5,5,5,5,21); $ls=@(32,32,32,32,16); $ws=@(16,16,16,16,256)
$below=0; $n16=[bigint]0; $n32=[bigint]0; $n512=[bigint]0; $n256=[bigint]0
for($i=0;$i -lt 5;$i++) {
    $keys=[bigint]::Pow(2,41-$below)
    $sub=[bigint]::Pow(2,41-$below-$hs[$i])
    $n16 += $keys*$ls[$i]*($ws[$i]-1)
    $n32 += $sub*([bigint]::Pow(2,$hs[$i])-1)
    if($i -eq 4){ $n256 += $keys } else { $n512 += $keys }
    $below += $hs[$i]
}
$n272=[bigint]::Pow(2,41)
$n16 += $n272*17*512; $n32 += $n272*17*511
$counts=@{ '16'=$n16; '32'=$n32; '512'=$n512; '256'=$n256; '272'=$n272 }
$expected=@{ '16'='20229886488608768'; '32'='19105114044235775'; '512'='2269957324800'; '256'='2097152'; '272'='2199023255552' }
$bits=@{ '16'=55; '32'=55; '512'=42; '256'=21; '272'=41 }
foreach($length in @('16','32','512','256','272')) {
    Check ($counts[$length].ToString() -eq $expected[$length]) ('class-size-'+$length)
    Check (($counts[$length] -le [bigint]::Pow(2,$bits[$length])) -and ($counts[$length] -gt [bigint]::Pow(2,$bits[$length]-1))) ('padded-bits-'+$length)
}
Check (($n16+$n32+$n512+$n256+$n272).ToString() -eq '39339469515522047') 'total-address-count'
$wt=[bigint]::Pow(2,21)*(16*255+1)+[bigint]::Pow(2,21)-1
Check (($wt-1).ToString() -eq '8560574462') 'strict-predecessor-cone'
Check (($wt+4*(32*(32*15+1)+31)+17*(512+511)+1).ToString() -eq '8560653547') 'routed-extraction-count'
Check ((4*(32*15-240)+(16*255-2040)+5+41+17*10+1) -eq 3217) 'accepted-digits-verifier-bound'
# Abstract witness predicate controls; no real h or cryptographic input is used.
function TcrPredicate([string]$genuine,[string]$actual,[string]$targetOutput,[string]$actualOutput) {
    return (($genuine -cne $actual) -and ($targetOutput -ceq $actualOutput))
}
Check (-not (TcrPredicate 'genuine' 'genuine' 'image' 'image')) 'same-hidden-input-is-not-TCR'
Check (TcrPredicate 'genuine' 'changed' 'image' 'image') 'different-input-equal-output-is-TCR'
Check (-not (TcrPredicate 'genuine' 'changed' 'image' 'other')) 'unequal-output-rejected'
# Collection exclusion is address-wide, not (address,length)-wide.
$target='selected-adrs'
$queries=@([pscustomobject]@{ Address='predecessor'; Length=16 },[pscustomobject]@{ Address='predecessor2'; Length=32 })
Check (-not (@($queries | ForEach-Object { $_.Address }) -ccontains $target)) 'legal-other-address-preparation'
$illegal=@([pscustomobject]@{ Address=$target; Length=32 })
Check (@($illegal | ForEach-Object { $_.Address }) -ccontains $target) 'selected-address-other-length-is-illegal'
# A finite selector enumeration confirms one first witness, not one hit per event.
$toyValid=5; $toyBits=3; $toyWitness=3; $wins=0
for($selector=0;$selector -lt [math]::Pow(2,$toyBits);$selector++) {
    if(($selector -lt $toyValid) -and ($selector -eq $toyWitness)){ $wins++ }
}
Check ($wins -eq 1) 'padded-selector-one-witness-one-win'
$result=[ordered]@{ classification='COMPUTED'; passed=$passed.Count; controls=$passed; construction='finite arithmetic and abstract game predicates only'; excludes='no source signing, hashing campaign, attack, full graph/cache, or benchmark' }
$result | ConvertTo-Json -Depth 5
