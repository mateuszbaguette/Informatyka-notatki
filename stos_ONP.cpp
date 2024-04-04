#include <iostream>
#include <cctype> //potrzebna dla funkcji  isdigit( int ch )
using namespace std;

struct element
{
 int wartosc;
 element *poprzedni;
};

element *dodaj (int liczba, element *wierzcholek)
{
 element *wsk;
 wsk = new element;
 if (!wsk) return 0;
 wsk->wartosc=liczba;
 wsk->poprzedni=wierzcholek;
 return wsk;
}

element *usun (int *liczba, element *wierzcholek)
{
 if (!wierzcholek) return 0;
 element *wsk;
 *liczba=wierzcholek->wartosc;
 wsk=wierzcholek->poprzedni;
 delete wierzcholek;
 return wsk;
}

void wypisz (element *wsk)
{
 cout<<"aktualny stos: ";
 while (wsk!=NULL)
 {
  cout<<wsk->wartosc<<"\t";
  wsk=wsk->poprzedni;
 }
 cout<<endl;
}

int main()
{
 //========= stos ========================
 /*
 int n, k;
 element *wierzcholek;
 wierzcholek=NULL;
 cout<<"WKLADANIE ELEMENTOW NA STOS"<<endl;
 cout<<"podaj, ile elementow wlozyc na stos: ";
 cin>>n;
 for(int i=0;i<n;i++)
 {
  cout<<"podaj liczbe calkowita: ";
  cin>>k;
  wierzcholek=dodaj(k,wierzcholek);
  wypisz(wierzcholek);
 }
 cout<<"\n\nUSUWANIE ELEMENTOW ZE STOSU"<<endl;
 while (wierzcholek!=NULL)
 {
  wierzcholek=usun(&k,wierzcholek);
  cout<<"zdejmowany element to: "<<k<<endl;
  wypisz(wierzcholek);
 }*/
 //===== ONP =======================================
 //string s="82-3/14+2*+6/";
 string s="252-*";
 cout<<s<<endl;
 int n=s.size(),k1,k2,w; // n=s.length();
 cout<<n<<endl;
 //==== deklaracja stosu=========================
 element *wierzcholek;
 wierzcholek=NULL;
 //=== jak dostac sie do łancucha ?==============
 cout<<s[0]<<endl;
 //====jesli s[i] jest liczba - odloz na stos============
 for(int i=0;i<n;i++){
    if ( isdigit(s[i])) {
    //cout<<"s["<<i<<"]-czy liczba"<<isdigit(s[i])<<endl;
    wierzcholek=dodaj((int)s[i]-48,wierzcholek);
    wypisz(wierzcholek);
    }
    else {
    //cout<<"s["<<i<<"]-czy liczba"<<isdigit(s[i])<<endl;
    k1=(int)s[i-1]-48;
    wierzcholek=usun(&k1,wierzcholek);
    wypisz(wierzcholek);
    k2=(int)s[i-2]-48;
    wierzcholek=usun(&k2,wierzcholek);
    wypisz(wierzcholek);
    //===jak zamiennic znak na operator =====
    switch (s[i]){
    case '+':w=k2+k1;break;
    case '-':w=k2-k1;break;
    case '*':w=k2*k1;break;
    case '/':w=k2/k1;break;
    }
    //===odloz na stos======================
    wierzcholek=dodaj(w,wierzcholek);
    wypisz(wierzcholek);
    }
 }

 return 0;
}

