TTMO'nun 2.ci toplantısında verdiği oyun crackleme meydan okumasının çözümü. Toplantıya katılmadım fakat bir arkadaşın ricası üzerine crackledim.

### Çözüm

Cracklemek için Cheat Engine kullandım. Öncelikle referenced strings
ile unregistered version referansını buldum

![](images/ref_str.png)

Referansı takip ettiğimde görüntüdeki yerin kontrol ettiğini gördüm

![](images/control_flow.png)

Bütün oyun kontrol için ilgili byte'ı okuduğu için byte'ı patchlediğim
anda oyun tamamen registered oldu. Patchlemek için Cheat Engine'nin Open File özelliğini kullanın, Create Process değil.

![](images/patch.png)

![](images/registered.png)