/* Restaurante SAVE — interacciones */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header sticky ---------- */
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('fijo', window.scrollY > 12);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Menú móvil ---------- */
  var hamb = document.querySelector('.hamb');
  var movil = document.querySelector('.menu-movil');
  if (hamb && movil) {
    var toggle = function (abrir) {
      hamb.setAttribute('aria-expanded', String(abrir));
      movil.classList.toggle('abierto', abrir);
      document.body.classList.toggle('menu-abierto', abrir);
      document.body.style.overflow = abrir ? 'hidden' : '';
    };
    hamb.addEventListener('click', function () {
      toggle(hamb.getAttribute('aria-expanded') !== 'true');
    });
    movil.addEventListener('click', function (e) {
      if (e.target.closest('a')) toggle(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && hamb.getAttribute('aria-expanded') === 'true') toggle(false);
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var revelables = document.querySelectorAll('.rv');
  if (revelables.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      revelables.forEach(function (el) { el.classList.add('visible'); });
    } else {
      var io = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add('visible');
            io.unobserve(en.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revelables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- FAQ acordeón ---------- */
  document.querySelectorAll('.faq__item').forEach(function (item) {
    var q = item.querySelector('.faq__q');
    var a = item.querySelector('.faq__a');
    if (!q || !a) return;
    q.addEventListener('click', function () {
      var abierto = item.getAttribute('data-abierto') === 'true';
      // cierra hermanos
      var lista = item.parentElement;
      lista.querySelectorAll('.faq__item[data-abierto="true"]').forEach(function (otro) {
        if (otro !== item) {
          otro.setAttribute('data-abierto', 'false');
          otro.querySelector('.faq__q').setAttribute('aria-expanded', 'false');
          otro.querySelector('.faq__a').style.maxHeight = '0px';
        }
      });
      item.setAttribute('data-abierto', String(!abierto));
      q.setAttribute('aria-expanded', String(!abierto));
      a.style.maxHeight = abierto ? '0px' : a.scrollHeight + 'px';
    });
  });
  window.addEventListener('resize', function () {
    document.querySelectorAll('.faq__item[data-abierto="true"] .faq__a').forEach(function (a) {
      a.style.maxHeight = a.scrollHeight + 'px';
    });
  });

  /* ---------- Nav de la carta (scroll-spy) ---------- */
  var cartaNav = document.querySelector('.carta-nav');
  if (cartaNav) {
    var enlaces = Array.prototype.slice.call(cartaNav.querySelectorAll('a[href^="#"]'));
    var secciones = enlaces
      .map(function (a) { return document.querySelector(a.getAttribute('href')); })
      .filter(Boolean);

    var marcar = function () {
      var limite = window.scrollY + 190;
      var activa = secciones[0];
      secciones.forEach(function (s) { if (s.offsetTop <= limite) activa = s; });
      enlaces.forEach(function (a) {
        var on = activa && a.getAttribute('href') === '#' + activa.id;
        a.classList.toggle('activo', on);
        if (on) {
          var caja = cartaNav.querySelector('.carta-nav__in');
          var izq = a.offsetLeft - caja.clientWidth / 2 + a.clientWidth / 2;
          caja.scrollTo({ left: izq, behavior: reduce ? 'auto' : 'smooth' });
        }
      });
    };
    var t = false;
    window.addEventListener('scroll', function () {
      if (!t) { t = true; requestAnimationFrame(function () { marcar(); t = false; }); }
    }, { passive: true });
    marcar();
  }

  /* ---------- Newsletter (demo) ---------- */
  document.querySelectorAll('.news').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = form.parentElement.querySelector('.news__ok');
      if (ok) { ok.style.display = 'block'; }
      form.reset();
    });
  });

  /* ---------- Formulario de reserva ---------- */
  var reservaForm = document.getElementById('form-reserva');
  if (reservaForm) {
    var selSucursal = reservaForm.querySelector('select[name="sucursal"]');

    // Preselecciona la sucursal si viene en la URL (?sucursal=av-patria)
    var pedida = new URLSearchParams(location.search).get('sucursal');
    if (pedida && selSucursal) {
      var opt = selSucursal.querySelector('option[data-id="' + pedida + '"]');
      if (opt) selSucursal.value = opt.value;
    }

    // La fecha mínima es hoy
    var fecha = reservaForm.querySelector('input[type="date"]');
    if (fecha) fecha.min = new Date().toISOString().slice(0, 10);

    reservaForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!reservaForm.checkValidity()) { reservaForm.reportValidity(); return; }
      var d = new FormData(reservaForm);
      var elegida = selSucursal && selSucursal.selectedOptions[0];
      var numero = (elegida && elegida.dataset.wa) || reservaForm.dataset.wa;
      var lineas = [
        'Hola SAVE, quiero reservar:', '',
        '• Sucursal: ' + (d.get('sucursal') || ''),
        '• Fecha: ' + (d.get('fecha') || ''),
        '• Hora: ' + (d.get('hora') || ''),
        '• Personas: ' + (d.get('personas') || ''),
        '• Nombre: ' + (d.get('nombre') || ''),
        '• Teléfono: ' + (d.get('telefono') || '')
      ];
      if (d.get('notas')) lineas.push('• Notas: ' + d.get('notas'));
      var texto = lineas.join('\n');
      window.open('https://wa.me/' + numero + '?text=' + encodeURIComponent(texto),
                  '_blank', 'noopener');
    });
  }

  /* ---------- Año dinámico ---------- */
  document.querySelectorAll('[data-anio]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
