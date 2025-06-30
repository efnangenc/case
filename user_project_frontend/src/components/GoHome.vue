<template>
    <div>

        <router-link to="/" class="home-button">
            <LeftArrowIcon class="leftarrow-icon" />
            <span>Go Home</span>
        </router-link>

    </div>
</template>

<script setup>
import LeftArrowIcon from '../assets/icons/left-arrow.svg'
import '../assets/styles/GoHomeButton.scss'
</script>
