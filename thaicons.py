{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMGMPDk2V508TldTCUJY1KU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sasipimpiangbunta/chula_eng/blob/main/thaicons.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import tkinter as tk\n",
        "import random\n",
        "import os\n",
        "\n",
        "# Check if the environment has a display\n",
        "if \"DISPLAY\" in os.environ:\n",
        "    # List of Thai consonants and their names\n",
        "    thai_consonants = [\n",
        "        (\"ก\", \"Gor Gai (ก ไก่)\"),\n",
        "        (\"ข\", \"Khor Khai (ข ไข่)\"),\n",
        "        (\"ค\", \"Khor Khuat (ค ขวด)\"),\n",
        "        (\"ง\", \"Ngor Ngu (ง งู)\"),\n",
        "        (\"จ\", \"Jor Jan (จ จาน)\"),\n",
        "        (\"ช\", \"Chor Chang (ช ช้าง)\"),\n",
        "        (\"ท\", \"Thor Thahan (ท ทหาร)\"),\n",
        "        (\"น\", \"Nor Nu (น หนู)\"),\n",
        "        (\"พ\", \"Phor Phan (พ พาน)\"),\n",
        "        (\"ม\", \"Mor Ma (ม ม้า)\"),\n",
        "        (\"ร\", \"Ror Rua (ร เรือ)\"),\n",
        "        (\"ล\", \"Lor Ling (ล ลิง)\"),\n",
        "        (\"ส\", \"Sor Suea (ส เสือ)\"),\n",
        "    ]\n",
        "\n",
        "    class FlashcardGame:\n",
        "        def __init__(self, root):\n",
        "            self.root = root\n",
        "            self.root.title(\"Thai Consonant Flashcard Game\")\n",
        "\n",
        "            self.current_card = None\n",
        "            self.is_flipped = False\n",
        "\n",
        "            self.card_frame = tk.Frame(root, width=300, height=200, bg=\"white\", relief=\"raised\", bd=5)\n",
        "            self.card_frame.pack(pady=20)\n",
        "\n",
        "            self.label = tk.Label(self.card_frame, text=\"\", font=(\"Arial\", 50), bg=\"white\")\n",
        "            self.label.pack(expand=True)\n",
        "\n",
        "            self.card_frame.bind(\"<Button-1>\", self.flip_card)\n",
        "            self.label.bind(\"<Button-1>\", self.flip_card)\n",
        "\n",
        "            self.next_button = tk.Button(root, text=\"Next Card\", command=self.next_card)\n",
        "            self.next_button.pack(pady=10)\n",
        "\n",
        "            self.next_card()\n",
        "\n",
        "        def next_card(self):\n",
        "            self.is_flipped = False\n",
        "            self.current_card = random.choice(thai_consonants)\n",
        "            self.label.config(text=self.current_card[0], font=(\"Arial\", 100))\n",
        "\n",
        "        def flip_card(self, event):\n",
        "            if not self.is_flipped:\n",
        "                self.label.config(text=self.current_card[1], font=(\"Arial\", 20))\n",
        "            else:\n",
        "                self.label.config(text=self.current_card[0], font=(\"Arial\", 100))\n",
        "            self.is_flipped = not self.is_flipped\n",
        "\n",
        "    if __name__ == \"__main__\":\n",
        "        root = tk.Tk()\n",
        "        game = FlashcardGame(root)\n",
        "        root.mainloop()\n",
        "else:\n",
        "    # If there is no display, print a message\n",
        "    print(\"No display found. GUI will not be shown.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ljyDZYzKXSuz",
        "outputId": "ca1763d2-1ecf-4726-8d39-f9fa1b4b31f4"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "No display found. GUI will not be shown.\n"
          ]
        }
      ]
    }
  ]
}