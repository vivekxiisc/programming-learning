document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // EMAILJS INIT
    // ==========================

    if (typeof emailjs !== "undefined") {
        emailjs.init("PcAez45zprj7jKMyP");
    }

    // ==========================
    // 3D TILT EFFECT
    // ==========================

    const tiltCards = document.querySelectorAll(
        ".tilt-card, .image-3d-card"
    );

    tiltCards.forEach(card => {

        card.addEventListener("mousemove", (e) => {

            const rect = card.getBoundingClientRect();

            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const rotateX =
                -(y - rect.height / 2) / 15;

            const rotateY =
                (x - rect.width / 2) / 15;

            card.style.transform = `
                perspective(1200px)
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                scale(1.03)
            `;
        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = `
                perspective(1200px)
                rotateX(0deg)
                rotateY(0deg)
                scale(1)
            `;
        });
    });

    // ==========================
    // CONTACT FORM
    // ==========================

    const contactForm =
        document.getElementById("contact-form");

    if (contactForm) {

        contactForm.addEventListener(
            "submit",
            function (e) {

                e.preventDefault();

                const submitBtn =
                    this.querySelector("button");

                submitBtn.innerHTML =
                    '<i class="fas fa-spinner fa-spin"></i> Sending...';

                emailjs.sendForm(
                    "vivekkumarsupport1308",
                    "template_5e8ckkp",
                    this
                )

                .then(() => {

                    submitBtn.innerHTML =
                        'Sent <i class="fas fa-check"></i>';

                    this.reset();

                    setTimeout(() => {

                        submitBtn.innerHTML =
                            'Transmit Package Payload <i class="fas fa-paper-plane"></i>';

                    }, 2500);

                })

                .catch((error) => {

                    console.error("Email Error:", error);

                    submitBtn.innerHTML =
                        'Retry <i class="fas fa-redo"></i>';

                });

            }
        );

        // ==========================
        // INPUTS & KEYBOARD FIX
        // ==========================

        const formInputs =
            contactForm.querySelectorAll(
                "input, textarea"
            );

        formInputs.forEach(input => {

            input.addEventListener(
                "mousedown",
                (e) => {
                    e.stopPropagation();
                }
            );

            input.addEventListener(
                "select",
                (e) => {
                    e.stopPropagation();
                }
            );

            input.addEventListener(
                "focus",
                () => {
                    input.selectionStart =
                        input.value.length;

                    input.selectionEnd =
                        input.value.length;
                }
            );

        });

        contactForm.addEventListener(
            "keydown",
            (e) => {

                if (e.key === "Tab") {

                    e.preventDefault();

                    const currentIndex =
                        Array.from(formInputs)
                        .indexOf(document.activeElement);

                    const nextIndex =
                        e.shiftKey
                            ? currentIndex - 1
                            : currentIndex + 1;

                    if (
                        nextIndex >= 0 &&
                        nextIndex < formInputs.length
                    ) {

                        formInputs[nextIndex].focus();

                    } else if (
                        nextIndex === formInputs.length
                    ) {

                        contactForm
                            .querySelector("button")
                            .focus();
                    }
                }
            }
        );
    }

    // ==========================
    // CONTACT BOX CLICK FIX
    // ==========================

    const contactBox =
        document.querySelector(
            ".contact-3d-box"
        );

    if (
        contactBox &&
        contactForm
    ) {

        const formInputs =
            contactForm.querySelectorAll(
                "input, textarea"
            );

        contactBox.addEventListener(
            "click",
            (e) => {

                if (
                    !e.target.closest(
                        "input, textarea, button"
                    )
                ) {

                    formInputs[0]?.focus();
                }
            }
        );
    }

    // ==========================
    // TYPEWRITER EFFECT
    // ==========================

    class TypeWriter {

        constructor(
            txtElement,
            words,
            wait = 3000
        ) {

            this.txtElement =
                txtElement;

            this.words =
                words;

            this.txt = "";

            this.wordIndex = 0;

            this.wait =
                parseInt(wait, 10);

            this.isDeleting = false;

            this.type();
        }

        type() {

            const current =
                this.wordIndex %
                this.words.length;

            const fullTxt =
                this.words[current];

            if (this.isDeleting) {

                this.txt =
                    fullTxt.substring(
                        0,
                        this.txt.length - 1
                    );

            } else {

                this.txt =
                    fullTxt.substring(
                        0,
                        this.txt.length + 1
                    );
            }

            this.txtElement.innerHTML =
                `<span class="txt">${this.txt}</span ><span class="cursor-pulse"></span>`;

            let typeSpeed = 80;

            if (this.isDeleting) {
                typeSpeed = 40;
            }

            if (
                !this.isDeleting &&
                this.txt === fullTxt
            ) {

                typeSpeed =
                    this.wait;

                this.isDeleting = true;

            } else if (
                this.isDeleting &&
                this.txt === ""
            ) {

                this.isDeleting = false;

                this.wordIndex++;

                typeSpeed = 200;
            }

            setTimeout(
                () => this.type(),
                typeSpeed
            );
        }
    }

    const txtElement =
        document.querySelector(
            ".typewriter"
        );

    if (txtElement) {

        const words =
            JSON.parse(
                txtElement.getAttribute(
                    "data-words"
                )
            );

        const wait =
            txtElement.getAttribute(
                "data-wait"
            ) || 3000;

        new TypeWriter(
            txtElement,
            words,
            wait
        );
    }

});
