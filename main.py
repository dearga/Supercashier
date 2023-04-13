{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04bdfe5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transaction import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "09de716b",
   "metadata": {},
   "outputs": [],
   "source": [
    "belanja=transaction()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bd85350b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  barang  price  qty  total\n",
      "0   baju  50000    1  50000\n",
      " \n",
      "Ditambahkan baju sejumlah 1 dengan harga satuan Rp 50000\n"
     ]
    }
   ],
   "source": [
    "belanja.add_item(\"baju\",50_000,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c1ce1923",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   barang  price  qty  total\n",
      "0    baju  50000    1  50000\n",
      "1  celana  80000    1  80000\n",
      " \n",
      "Ditambahkan celana sejumlah 1 dengan harga satuan Rp 80000\n"
     ]
    }
   ],
   "source": [
    "belanja.add_item(\"celana\",80_000,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e0e74c74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   barang  price  qty  total\n",
      "0    baju  50000    1  50000\n",
      "1  celana  80000    1  80000\n",
      " \n",
      "Daftar belanjaan sudah benar.\n"
     ]
    }
   ],
   "source": [
    "belanja.check_order()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f7892145",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   barang  price  qty  total\n",
      "0  celana  80000    1  80000\n",
      "1    kaos  50000    1  50000\n",
      " \n",
      "Nama barang baju diupdate menjadi kaos\n"
     ]
    }
   ],
   "source": [
    "belanja.update_item_name(\"baju\",\"kaos\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "69251223",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   barang  price  qty  total\n",
      "0  celana  80000    1  80000\n",
      "1    kaos  50000    1  50000\n"
     ]
    }
   ],
   "source": [
    "belanja.show_order()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "48ad8ed2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   barang   price  qty   total\n",
      "0  celana  200000    1  200000\n",
      "1    kaos   50000    1   50000\n",
      " \n",
      "Harga Celana diperbaharui dari Rp 150000 menjadi Rp 200000\n"
     ]
    }
   ],
   "source": [
    "belanja.update_item_price(\"Celana\",200_000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "870b9ed3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   barang   price  qty   total\n",
      "0  celana  200000    1  200000\n",
      "1    kaos   50000    1   50000\n",
      " \n",
      "Total harga adalah Rp250000, diskon sebesar Rp12500 dan total harga akhir sebesar Rp237500\n"
     ]
    }
   ],
   "source": [
    "belanja.total_price()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "547fce58",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
