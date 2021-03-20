//Tarea_2 Milton Cárdenas y Sebastián Picado
//Se incluyen las librerías necesarias
#include <chrono>
#include <math.h>
#include <iostream>
#include <pthread.h>

//Se da acceso al espacio de nombres

using namespace std;
using namespace std::chrono;

//Se inicializan las variables

int array [10000000];
int i = 0;
int k = 0;
int a = 0;
int b = 2500000;
int c = 5000000;
int d = 7500000;
int potencia = 0;

//Se inicializan los hilos

pthread_t h1;
pthread_t h2;
pthread_t h3;
pthread_t h4;
pthread_t h5;

//Se inicializa la función para el manejo de zonas de acceso exclusivo

pthread_mutex_t lock;

//Se inicializan los punteros

int *registro1[10000000];
int *registro2[10000000];
int *registro3[10000000];
int *registro4[10000000];
int *registro5[10000000];

//Funciones para los hilos

/*Se encarga de calcular la potencia de cada elemento
del array*/

void *hilo_1(void *arg){
  int *registro1 = (int*) arg;
  while (i<=9999999) {
    potencia = pow(registro1[i],2);
    i++;
  }
  cout<< "Listo hilo_1" << endl;
  pthread_exit(NULL);

}

/*Se encarga de calcular la potencia de los elementos del 0 al
2499999 del array*/

void *hilo_4a(void *arg){
  int *registro2 = (int*) arg;
  while (a<=2499999) {
    potencia = pow(registro2[a],2);
    a++;
  }
  cout<< "Listo hilo_4a" << endl;
  pthread_exit(NULL);

}

/*Se encarga de calcular la potencia de los elementos del 2500000 al
4999999 del array*/

void *hilo_4b(void *arg){

  int *registro3 = (int*) arg;
  while (b<=4999999) {
    potencia = pow(registro3[b],2);
    b++;
  }
  cout<< "Listo hilo_4b" << endl;
  pthread_exit(NULL);
}

/*Se encarga de calcular la potencia de los elementos del 4500000 al
7499999 del array*/

void *hilo_4c(void *arg){

  int *registro4 = (int*) arg;
  while (c<=7499999) {
    potencia = pow(registro4[c],2);
    c++;
  }
  cout<< "Listo hilo_4c" << endl;
  pthread_exit(NULL);
}

/*Se encarga de calcular la potencia de los elementos del 7500000 al
9999999 del array*/

void *hilo_4d(void *arg){

  int *registro5 = (int*) arg;
  while (d<=9999999) {
    potencia = pow(registro5[d],2);
    d++;
  }
  cout<< "Listo hilo_4d" << endl;
  pthread_exit(NULL);
}

//Funcion principal

//Se crea el array de 10000000 de elementos distintos

int main()
 {
  while (k<=9999999)
   {
    array[k] = k;
    k++;
   }

//Se inicia la instrucción dentro del hilo y el cronómetro

  auto start_1 = high_resolution_clock::now();

  pthread_create(&h1, NULL, hilo_1, array);
  pthread_join(h1, NULL);

  auto stop_1 = high_resolution_clock::now();
  auto duration_1 = duration_cast<milliseconds>(stop_1 - start_1);

//Se imprime el tiempo de ejecución para un único hilo

  cout << "La duración con 1 núcleo es de: " << duration_1.count() << " milisegundos." << endl;

  auto start_4 = high_resolution_clock::now();

//Se inician la instrucción dentro de los cuatros hilos y el cronómetro

  pthread_create(&h2, NULL, hilo_4a, array);
  pthread_create(&h3, NULL, hilo_4b, array);
  pthread_create(&h4, NULL, hilo_4c, array);
  pthread_create(&h5, NULL, hilo_4d, array);

  pthread_join(h2, NULL);
  pthread_join(h3, NULL);
  pthread_join(h4, NULL);
  pthread_join(h5, NULL);

  auto stop_4 = high_resolution_clock::now();

  auto duration_4 = duration_cast<milliseconds>(stop_4 - start_4);

//Se imprime el tiempo de ejecución para 4 hilos

  cout << "La duración con 4 núcleos es de: " << duration_4.count() << " milisegundos." << endl;

  return 0;
}
